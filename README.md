### Installation
```
bash install.sh
```

### Usage
```
usage: selfie [-h] [-d DEVICE] [-o OUTPUT] [--show] [--skip-save]

Take selfies of yourself

optional arguments:
-h, --help                   Show this help message and exit
-d DEVICE, --device DEVICE   Video device to take picture
-o OUTPUT, --output OUTPUT   Directory to dump selfie
--show                       Display image after taking selfie
--skip-save                  Skip saving the image
```

Example:
```
selfie --device /dev/video2 --output /media/m/XHD/selfies
```

Or, put it in your .bashrc:

```
# Take a selfie everytime I source my .bashrc.  I'll see how I age overtime. Yikes!
$(selfie --device /dev/video2 --output $HOME/Dropbox/selfies &>/dev/null &)

```
