import os
import shutil
import hashlib
from PIL import Image

# up to 9999 wallpers
user_path = os.getenv("USERPROFILE")

# default directory, this folder will be created if doesn't exits
wallpaper_dir = os.path.join(user_path, "Pictures", "WinWallpaper")

# asset directory
# in this directory are contained windows lockscreen wallpapers and some other stuff
asset_dir = os.path.join(user_path, "AppData", "Local", "Packages", "Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy", "LocalState", "Assets")

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



print("Keep phone wallpapers? [Y/N] - Default no")
get_phone = input()

# ask to keep phone wallpapers too
if get_phone.upper() == "Y":
    get_phone = True
else:
    get_phone = False

# creation of destination folder if doesn't exists
if not os.path.isdir(wallpaper_dir):
    os.mkdir(wallpaper_dir)
    print("Destination folder not found. Folder " + wallpaper_dir + " created.")

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
    wallpaper_name ="Lockscreen"+ str(init_count).rjust(5, "0") + ".jpg"
    print("Added " + wallpaper_name)
    os.rename(os.path.join(wallpaper_dir, file_list_asset[i].name), os.path.join(wallpaper_dir, wallpaper_name))
    init_count += 1


input("Press any key to exit...")
