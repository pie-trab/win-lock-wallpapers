import os
import shutil
from PIL import Image

userPath = os.getenv('USERPROFILE')

# up to 9999 wallpers

# destination directory, the folder will be created if doesn't exits
wallpaperDir = userPath + '\\Pictures\\WinWallPapers'

# asset dyrectory where the lockscreen files are stored
assetsDir = userPath + \
    '\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'


def checkAspectRatio(file):
    if (Image.open(file).size[0] != 1920):
        return False
    else:
        return True


def justifiesName(number):
    return str(number).rjust(4, "0")


def getWallpaper():
    # get a list of all files of the directory assets on form of direntry
    fileListAsset = []
    for i in os.scandir(assetsDir):
        if i.is_file():
            fileListAsset.append(i)

    # creation of destination folder if doesn't exists
    if (not os.path.isdir(wallpaperDir)):
        os.mkdir(wallpaperDir)

    # get a list of all files of the directory desktop on form of direntry
    fileListWallpaper = []
    for i in os.scandir(wallpaperDir):
        if i.is_file() and i.name:
            fileListWallpaper.append(i)

    isEqual = False
    for i in fileListAsset:
        for j in fileListWallpaper:
            if (open(i, 'rb').read() == open(j, 'rb').read()):
                isEqual = True
                if (i.name != j.name):
                    print(i.name + ' is the same as ' + j.name)
        if (not isEqual) and checkAspectRatio(i.path):
            shutil.copy(i.path, wallpaperDir)
            filesNumber = len(os.listdir(wallpaperDir)) - 1
            print(filesNumber)
            os.rename(wallpaperDir + '\\' + i.name, wallpaperDir + '\\' +
                      'Lockscreen' + justifiesName((filesNumber + 1)) + '.jpg')
        isEqual = False


getWallpaper()
input("Press any key to exit...")
