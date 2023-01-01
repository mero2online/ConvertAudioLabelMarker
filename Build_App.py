import PyInstaller.__main__
import os
import shutil
from settings import appVersionNo
from platform import release, architecture

cwd = os.getcwd()
wd = f'{cwd}\\dist'
outputFileName = f'ConvertAudioLabelMarker_v{appVersionNo}-Win_{release()}-{architecture()[0]}'


def clean():
    dirsToRemove = [f'{cwd}\\build', f'{cwd}\\__pycache__']
    for d in dirsToRemove:
        if os.path.exists(d):
            shutil.rmtree(d)

    for file_name in os.listdir(cwd):
        pathOnly, file_extension = os.path.splitext(file_name)
        file = f'{cwd}\\{file_name}'
        if os.path.isfile(file) and file_extension == '.spec':
            os.remove(file)


clean()

PyInstaller.__main__.run([
    'ConvertAudioLabelMarker.py',
    f'-n{outputFileName}',
    '--onefile',
    '--windowed',
    '--add-data', 'src;src',
    '-i', ".\src\\label_icon.ico",
    '--splash', ".\src\\label_icon.png",
    '--exclude-module', 'matplotlib'
])

clean()
os.startfile(wd)
