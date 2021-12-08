
#!/usr/bin/python
from PIL import Image
import os, sys
import subprocess

path = "../../downloads/test2/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        extension = os.path.splitext(item)[-1].lower()
        if extension == '.jpg':
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((518,388), Image.ANTIALIAS)
            imResize.save(path + 'Resized/' + item , 'JPEG', quality=90)

resize()