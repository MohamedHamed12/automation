import os
import subprocess
import sys


def get_files(path):
    files = []
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            files += get_files(full_path)
        else:
            files.append(full_path)
    return files

directory  = sys.argv[1]
path=os.getcwd()
for file in get_files(directory):

       subprocess.Popen(["xdg-open", str(file)])


