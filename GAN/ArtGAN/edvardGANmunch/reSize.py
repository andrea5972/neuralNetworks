"""
Preprocess.py
Resize all of the downloaded images to desired dimension
(DEFAULT 32,32 pixels)
Renames images in folders to .png
"""

import os
import random
import scipy.misc
import imageio

root='./fullimages'

PATH = 'Edvard_Munch/'
OUT = 'Edvard_Munch/resized/'

for f in os.listdir(PATH):
    if os.path.isfile(os.path.join(PATH, f)):
        i = 0
        source = PATH + f
        print(str(i) + f)
        try:
            print(source)
            image = imageio.imread(source)
            image = scipy.misc.imresize(image,(32,32))
            scipy.misc.imsave(OUT + str(i) + '.png',image)
            i+=1
        except Exception as e:
            print('missed it: ' + source)
            print(e)
        i = i + 1
