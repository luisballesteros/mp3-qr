import os
import glob
import re

dir_actual = os.getcwd()

path = os.getcwd()

for filename in glob.glob(path + '\\*'):
    # pattern = r'\s'
    # replace = r'_'
    pattern = r'_-'
    replace = r'_'
    new_name = re.sub(pattern, replace, filename)
    print(filename + ' -> ' + new_name)
    os.rename(filename, new_name)


wav_list = os.listdir(dir_actual)
print(wav_list)
