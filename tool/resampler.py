import subprocess
import os

def resample(inp, otp):

    input_path = inp
    output_path = otp
    
    file1 = input_path + 'tempvoice.wav'
    file2 = output_path + 'tempvoice.wav'
    cmd = "ffmpeg -i " + file1 + " -ar 32000 " + file2 
    subprocess.call(cmd, shell=True)
