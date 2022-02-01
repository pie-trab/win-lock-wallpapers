import os
import shutil
from PIL import Image

# destination directory chosen by the user
wallpaperDir = 'C:\\Users\\Pietro\\Pictures\\Sfondi\\Sfondi_Windows10'

# asset dyrectory where the lockscreen files are stored
assetsDir = 'C:\\Users\\Pietro\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'


def checkAspectRatio(file):
    if (Image.open(file).size[0] != 1920):
        return False
    else:
        return True


def giustificaNome(number):
    return str(number).rjust(4, "0")


def ricavaSfondi():
    # get a list of all files of the directory assets on form of direntry
    fileListAsset = []
    for i in os.scandir(assetsDir):
        if i.is_file():
            fileListAsset.append(i)

    # get a list of all files of the directory desktop on form of direntry
    fileListWallpaper = []
    for i in os.scandir(wallpaperDir):
        if i.is_file() and i.name != 'confronta.py':
            fileListWallpaper.append(i)

    isEqual = False
    for i in fileListAsset:
        for j in fileListWallpaper:
            if (open(i, 'rb').read() == open(j, 'rb').read()):
                isEqual = True
                if (i.name != j.name):
                    print(i.name + ' uguale a ' + j.name)
        if (not isEqual) and checkAspectRatio(i.path):
            shutil.copy(i.path, wallpaperDir)
            filesNumber = len(os.listdir(wallpaperDir)) - 1
            print(filesNumber)
            os.rename(wallpaperDir + '\\' + i.name, wallpaperDir + '\\' +
                      'Lockscreen' + giustificaNome((filesNumber + 1)) + '.jpg')
        isEqual = False


ricavaSfondi()
input("Premi un tasto per continuare...")
