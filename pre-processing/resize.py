64

#!/usr/bin/python
from PIL import Image
import os, sys

path = "../../downloads/object-labeling/vott-csv-export/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((518,388), Image.ANTIALIAS)
            imResize.save(path + 'Resized/' + item , 'JPEG', quality=90)

resize()