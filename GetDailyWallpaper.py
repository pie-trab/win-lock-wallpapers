import os
import shutil
import hashlib
from PIL import Image

userPath = os.getenv("USERPROFILE")

# up to 9999 wallpers

# destination directory, the folder will be created if doesn't exits
wallpaperDir = userPath + "\\Pictures\\Sfondi\\Sfondi_Windows10"

# asset dyrectory wherse the lockscreen files are stored
assetsDir = (
    userPath
    + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
)


def checkAspectRatio(file, get_mobile):
    """ Checks the aspect ratio of the input file

    Args:
        file (str): file path
        get_mobile (bool): True - keeps mobile wallpapers, False - discards mobile wallpapers

    Returns:
        bool: the file is a wallpaper
    """
    return Image.open(file).size[0] == 1920 or (get_mobile and Image.open(file).size[1] == 1920)


def justifiesName(number):
    """ Justifies the file name to accomodate up to 9999 walpapers

    Args:
        number (int): number of the walpaper

    Returns:
        str: justified number
    """
    return str(number).rjust(4, "0")


# computes the hash of the file
def get_sha256(file):
    """ Computes the md5 hash of the file

    Args:
        file (str): file path

    Returns:
        str: the hexadecimal digest of the hash
    """
    BLOCK_SIZE = 65536  # The size of each read from the file

    # Create the hash object, can use something other than `.sha256()` if you wish
    file_hash = hashlib.sha256()
    with open(file, 'rb') as f:  # Open the file to read it's bytes
        # Read from the file. Take in the amount declared above
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:  # While there is still data being read from the file
            file_hash.update(fb)  # Update the hash
            fb = f.read(BLOCK_SIZE)  # Read the next block from the file

    return file_hash.hexdigest()  # Get the hexadecimal digest of the hash


def not_intersect(dict1, dict2):
    """ Intersection of two dictionaries

    Args:
        dict1 (dict): 
        dict2 (dict): second dictionary

    Returns:
        dict: not intesection
    """
    temp = {}

    for i in dict1:
        if not (i in dict2):
            temp[i] = dict1[i]

    return temp


# main stuff
def getWallpaper():
    # creation of destination folder if doesn't exists
    if not os.path.isdir(wallpaperDir):
        os.mkdir(wallpaperDir)

    # dictionary of all files respecting aspect ratio in asset directory direntry
    fileListAsset = {}
    for i in os.scandir(assetsDir):
        if i.is_file() and checkAspectRatio(i.path, False):
            fileListAsset[get_sha256(i.path)] = i

    # dictionary of all files in desktp directory direntry
    fileListWallpaper = {}
    for i in os.scandir(wallpaperDir):
        if i.is_file():
            fileListWallpaper[get_sha256(i.path)] = i

    toMove = not_intersect(fileListAsset, fileListWallpaper)

    initCount = len(fileListWallpaper) + 1

    for i in toMove:
        shutil.copy(toMove[i].path, wallpaperDir)
        print("Lockscreen" + justifiesName(initCount) + ".jpg")
        os.rename(wallpaperDir + "\\" +
                  toMove[i].name, wallpaperDir + "\\" + "Lockscreen" + justifiesName(initCount) + ".jpg")
        initCount += 1


getWallpaper()
input("Press any key to exit...")
