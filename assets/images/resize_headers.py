#!/usr/bin/env python

"""
A small script to resize header images to no more than 1920 pixels wide.
"""
import os
from PIL.Image import open, BILINEAR

images = os.listdir('headers')
for i, image in enumerate(images):
    image = os.path.join('headers', image)
    try:
        image_ = open(image)
        print('[ {} | {} ] Processing: {}'.format(i,
                                                  len(images),
                                                  image.lower()), end=', ')
    except OSError:
        continue
    if image_.width > 1920:
        print('resizing...', end=',')
        scale_factor = image_.width / 1920.
        height = int(image_.height / scale_factor)
        new_image = image_.resize((1920, height), BILINEAR)
        new_image.save(image.lower())
        print('{} saved.'.format(image))
    else:
        print('no resizing needed.')

    os.rename(image, image.lower())
