
import os
from pydub import AudioSegment
 
def voice_reformat(source, target, file, source_form = "flac", target_form="wav"):

    length = len(source_form)
    if source_form == "flac":
        song = AudioSegment.from_file(source+file)     #读取音频文件
    elif source_form == "mp3":
        song = AudioSegment.from_mp3(source+file)
    elif source_form == "wav":
        song = AudioSegment.from_wav(source+file)
    elif source_form == "ogg":
        song = AudioSegment.from_ogg(source+file)
    else:
        print("没有这种格式！")
    song.export(target+f"{file[:-length]}"+target_form,format=target_form)
