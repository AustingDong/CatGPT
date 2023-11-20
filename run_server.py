from text.spider_v3 import process_messages
from tts.text_to_sound import tts
from tts.tts_APIver import tts_api, get_access_token
import json
import subprocess
import os
import shutil
import openai
import time
from tool.resampler import resample
from tool.audioplayer import play
from tool.reformat import voice_reformat

from flask import Flask, Response, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

from starlette.middleware.cors import CORSMiddleware
# CatGPT Objects:
from CatGPT_Objects.communication import Communication, CommunicationSchema
from CatGPT_Objects.singing import Singing

#tts_VITS
from tts.tts_vits import tts_vits

app = Flask(__name__)
api = Api(app)
CORS(app)


def run():
    subprocess.run('python voice/inference_main.py')

@app.route("/chat/", methods=['POST'])
def chat():
    data = request.get_json()
    schema = CommunicationSchema()
    communication = schema.load(data)

    text = communication['text']
    language = communication['language']
    messages = process_messages(text, language, mode='cat')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True
    )

    def generate():
        text_segment = ""
        seg_cnt = 0
        element_cnt = 0
        server_response = {
            'text': "",

        }
        for trunk in response:
            if trunk['choices'][0]['delta'] != {} and trunk['choices'][0]['delta']['content'] != "。" and element_cnt < 20:
                text_segment += trunk['choices'][0]['delta']['content']
            else:
                if trunk['choices'][0]['delta'] != {}:
                    text_segment += trunk['choices'][0]['delta']['content']
                element_cnt = 0
                seg_cnt += 1
                print(text_segment)
                # q.put(text_segment)
                server_response['text'] = text_segment
                yield json.dumps(server_response['text']) + '\n'
                if communication['sound']:

                    tts_vits(text_segment, language)
         
                    play('tts_vits.wav')
                    time.sleep(0.1)

                # (consider async) --> redis queue
                # asyncio.run(process_queue())
                # asyncio.run(tts_api(text_segment, seg_cnt))
                # asyncio.run(play(str(seg_cnt) + ".wav"))

                text_segment = ""
            
    headers = {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'X-Accel-Buffering': 'no',
    }
    return Response(generate(), mimetype="text/event-stream", headers=headers)


@app.route("/sing/", methods=['POST'])
def sing(singing: Singing):
    if singing.file == None:
        text = singing.send
        filepath = text.split("-")[1]
        filepath.strip('\'')
        shutil.copyfile(filepath, './voice/raw/tempvoice.wav')
        run()

        source_dir = './voice/results/'
        target_dir = './result/'
        filename = 'tempvoice_0key_Ayaka'
        suffix = '.flac'
        reformatted_suffix = '.wav'
        voice_reformat(source_dir, target_dir, filename+suffix)

        print("start playing...")
        
        play(filename+reformatted_suffix)
        os.remove("./result/"+filename+reformatted_suffix)
    return {"reply": "Wow~"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    