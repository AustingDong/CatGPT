import sounddevice as sd
import soundfile as sf

def play(target):
    data, samplerate = sf.read(f'./result/{target}', dtype='float32')

    sd.play(data, samplerate)

    sd.wait()