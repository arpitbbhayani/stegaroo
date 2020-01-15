import os
import sys
from PIL import Image

LSB_MASK = {
  1: (1 << 1) - 1,
  2: (1 << 2) - 1,
  3: (1 << 3) - 1,
  4: (1 << 4) - 1,
  5: (1 << 5) - 1,
  6: (1 << 6) - 1,
  7: (1 << 7) - 1,
  8: (1 << 8) - 1,
}

def get_bits(text):
  """get_bits creates and returns the bit stream from text and returns the
  list containing bits as string.
  """
  return list(''.join([bin(b)[2:].zfill(8) for b in
              bytes(text.encode('utf-8'))]))


def new_image(old_im):
  """The function writes pixel_map at path
  """
  return Image.new(old_im.mode, old_im.size)


def conceal(in_path, out_path, text):
  in_img, pixel_map = read_image(in_path)
  out_img = new_image(in_img)

  for i in range(in_img.size[0]):
    for j in range(in_img.size[1]):
      out_img.putpixel((i, j), pixel_map[i,j])

  with open(out_path, 'wb') as fp:
    out_img.save(fp)
    out_img.close()


def read_image(path):
  """The function read_image, reads the image from the path `path`
  and returns the pixel map loaded in memory.

  Any exceptions raised by PIL library are unhandled.
  """

  # open the image given the path
  im = Image.open(path)

  # load the pixel map.
  pixel_map = im.load()

  # log some meta information about the image
  print('the image read from path {} has following properties'.format(path))
  print('size: {} x {}'.format(*im.size))
  print('format: {}'.format(im.format))

  # close the file. always.
  im.close()

  # return the pixel map.
  return im, pixel_map


conceal(sys.argv[1], sys.argv[2], "arpit")
