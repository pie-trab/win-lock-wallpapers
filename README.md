# win-lock-wallpapers

This script allows to get Windows lockscreen wallpaper

```python
# asset dyrectory wherse the lockscreen files are stored 
asset_dir = user_home / 'AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'
```

After discarding some useless files (in this directory are stored the banner for the preinstalled ads in windows and other stuff) moves the wallpapers to the output directory.

## Requirements 

Install [PIL](https://pypi.org/project/pillow/) library.

```
pip install PIL
```

## Usage

Set the wallpaper dir to whatever you like the default is under "user\Pictures\LockScreenWallpapers" and it will be automatically created

```python
# destination directory, the folder will be created if doesn't exits
user_home / 'win-lock-wallpapers'.mkdir(parents=True, exist_ok=True)
# e.g.
# C:\Users\[user-name]\Pictures\win-lock-wallpapers
```
Then execute the script.
