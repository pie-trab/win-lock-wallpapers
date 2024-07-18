# win-lock-wallpapers

This script allows to get Windows lockscreen wallpaper

```python
# asset dyrectory wherse the lockscreen files are stored 
asset_dir = os.path.join(user_path, "AppData", "Local", "Packages", "Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy", "LocalState", "Assets")
```

After discarding some useless files (in this directory are stored the banner for the preinstalled ads in windows and other stuff) moves the wallpapers to a user set directory.

## Requirements

You will need the [PIL ](https://pypi.org/project/pillow/)library.

## Usage

Set the wallpaper dir to whatever you like the default is under "user\Pictures\LockScreenWallpapers" and it will be automatically created

```python
# destination directory, the folder will be created if doesn't exits
wallpaper_dir = os.path.join(user_path, "Pictures", "WinWallpaper")
```

After that, simply execute the program however you like.
