import os
from pathlib import Path
import shutil
import hashlib
from PIL import Image

# up to 9999 wallpers (5 zeros)
rjust_padding = 5

user_home = Path.home() 

# asset directory
# in this directory are contained windows lockscreen wallpapers and some other stuff
asset_dir = user_home / 'AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'

user_home = user_home / 'Pictures'

def valid_wallpaper(file, get_mobile):
    """ Checks the aspect ratio to discard usless images and optionally mobile wallpapers (1080x1920 vertical)

    Args:
        file (str): file path
        get_mobile (bool): True - keep, False - discards

    Returns:
        bool: True - valid wallpaper, False - invalid wallpaper
    """
    return Image.open(file).size[0] == 1920 or (get_mobile and Image.open(file).size[1] == 1920)


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


def main():
    print("Keep phone wallpapers? [N/y]")
    get_phone = input()

    # ask to keep phone wallpapers too
    try:
        get_phone = get_phone[0].upper() == "Y"
    except IndexError:
        get_phone = False

    # creation of destination folder if doesn't exists
    # default directory, this folder will be created if doesn't exits
    wallpaper_dir = user_home / 'win-lock-wallpapers'

    if not wallpaper_dir.exists():
        user_home / 'win-lock-wallpapers'.mkdir(parents=True, exist_ok=True)
        print(f'Output folder created at {user_home}')
    else:
        print(f'Output folder found at {user_home}')

    # all file in asset
    file_list_asset = {}
    for i in os.scandir(asset_dir):
        if i.is_file() and valid_wallpaper(i.path, get_phone):
            file_list_asset[get_sha256(i.path)] = i

    # all files alredy in wallpaper dir
    file_list_wallpaper = {}
    for i in os.scandir(wallpaper_dir):
        if i.is_file():
            file_list_wallpaper[get_sha256(i.path)] = i

    # finds the intersection of the two dictionaries   
    to_move = file_list_asset.keys() - file_list_wallpaper.keys()

    init_count = len(file_list_wallpaper) + 1

    # move and rename all not duplicate wallpaper
    for i in to_move:
        shutil.copy(file_list_asset[i].path, wallpaper_dir)
        wallpaper_name ="Lockscreen"+ str(init_count).rjust(rjust_padding, "0") + ".jpg"
        print("Added " + wallpaper_name)
        os.rename(os.path.join(wallpaper_dir, file_list_asset[i].name), os.path.join(wallpaper_dir, wallpaper_name))
        init_count += 1


    input("Press any key to exit...")

main()