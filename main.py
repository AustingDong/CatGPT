from text.spider_v3 import GPT
from tts.text_to_sound import tts
from tts.tts_APIver import tts_api, get_access_token
import json
import subprocess
import os
import shutil

from tool.resampler import resample
from voice.inference_main import run
from tool.audioplayer import play
from tool.reformat import voice_reformat

if __name__ == '__main__':

    text = ""

    while text != "stop":

        text = input("Me:")


        if text.split(":")[0] == 'path':
            filepath = text.split(":")[1]
            filepath.strip('\'')
            shutil.copyfile(filepath, './voice/raw/tempvoice.wav')

        else:
            res = GPT(text, mode='cat')

            print("\n\n猫猫:",res,"\n\n")

            token = get_access_token()
            tts_api(token, res)

            
            if os.path.exists('./voice/raw/tempvoice.wav'):
                os.system(f'rm -f ./voice/raw/tempvoice.wav')
            resample('./tts/temp/', './voice/raw/')

        
        run()

        source_dir = './voice/results/'
        target_dir = './result/'
        filename = 'tempvoice_0key_speaker0'
        suffix = '.flac'
        reformatted_suffix = '.wav'
        voice_reformat(source_dir, target_dir, filename+suffix)

        print("start playing...")
        play(filename+reformatted_suffix)

        # os.system(f'rm -f {target_dir+filename+reformatted_suffix}')








