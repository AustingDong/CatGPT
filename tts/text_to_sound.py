import pyttsx3
import os
from ffmpy import FFmpeg as mpy

path = './so-vits-svc-32k/raw/rawvoice.mp3'
transfered_path = './so-vits-svc-32k/raw/rawvoice.mp3'

def mp3_to_wav(mp3_file):
    cmder = '-f wav -ac 1 -ar 16000'
    mpy_obj = mpy(
        inputs={
            mp3_file: None
        },
        outputs={
            transfered_path: cmder
        }
    )
    mpy_obj.run()
    

def tts(text):

    text = text.replace('\n', '')
    engine = pyttsx3.init()

    engine.setProperty('rate', 200)
    engine.setProperty('volume', 0.8)

    # voices = engine.getProperty('voices')

    # engine.setProperty('voice', voices[0].id)
    # engine.say(text)

    engine.save_to_file('Ok, I saved it', filename='test.wav')
    engine.runAndWait()
    # mp3_to_wav(path)



