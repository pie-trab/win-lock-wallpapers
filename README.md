# win-lock-wallpapers

This simple script gets the lockscreen wallpapers from the Assets dir in the AppData folder

`# asset dyrectory wherse the lockscreen files are stored assetsDir = (     userPath     + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets" )`

After discarding some useless files (in this directory are stored the banner for the preinstalled ads in windows) moves the wallpapers to a user set directory.

## Usage

Set the wallpaper dir to whatever you like the default is under "user\Pictures\LockScreenWallpapers" and it will be automatically created

`# destination directory, the folder will be created if doesn't exits wallpaperDir = userPath + "\\Pictures\\Sfondi\\Sfondi_Windows10"`

After that, simply execute the program as you like.
