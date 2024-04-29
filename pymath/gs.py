#!/usr/bin/env python

## Convert color image to grayscale
import PIL.Image as Img
im0 = Img.open('ShivaPassportPic.jpg')
print(im0.size , im0.mode)
im1 = im0.convert('L')
im1.thumbnail((100, 100))
print(im1.size , im1.mode)
im1.save('SPP.jpg')
