
#!/usr/bin/python
from PIL import Image
import os, sys
import subprocess

path = "../../Documents/extraction/MISC/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        extension = os.path.splitext(item)[-1].lower()
        if extension == '.jpg':
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((52,52), Image.ANTIALIAS)
            imResize.save(path + 'Resized/' + item , 'JPEG', quality=90)

resize()