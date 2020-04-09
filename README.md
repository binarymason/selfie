### Installation
```
bash install.sh
```

### Usage
```
usage: selfie.py [-h] [-d DEVICE] [-o OUTPUT] [--show] [--skip-save]

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
python3 selfie.py --device /dev/video2 --output /media/m/XHD/selfies
```
