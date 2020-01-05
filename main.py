import os
import sys
from PIL import Image

with Image.open(sys.argv[1]) as im:
  print(os.path.basename(im.fp.name))
  print(os.path.dirname(im.fp.name))
  print(im.format, im.size, im.mode)

  pixelMap = im.load()
  img = Image.new( im.mode, im.size)
  pixelsNew = img.load()
  for i in range(img.size[0]):
    for j in range(img.size[1]):
        if 205 in pixelMap[i,j]:
            pixelMap[i,j] = (0,0,0,255)
        else:
            pixelsNew[i,j] = pixelMap[i,j]

img.show()
