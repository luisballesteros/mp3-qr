from pydub import AudioSegment
import os
import glob

path = os.getcwd()
print(path)

for filename in glob.glob(path + '\\*'):
    if filename.endswith(".wav"):
        # print(filename)
        new_name = filename[:-4]
        # print(new_name)
        # De wav a mp3
        song = AudioSegment.from_wav(filename)
        # print(song)
        song.export(new_name+".mp3", format="mp3")
#song = AudioSegment.from_file(file="pag_06_1.wav", format="wav")
# song = AudioSegment.from_wav("/pag_06_1.wav")
#song.export(out_f="pag_06_1.mp3", format="mp3")
