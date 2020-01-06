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

def get_bits(text, grouping=1):
  b = ''.join([bin(b)[2:] for b in bytes(text.encode('utf-8'))])
  for i in range(0, len(b), nb):
    yield b[i:i+nb]


def set_lsb(num, bits):
  return num | LSB_MASK[len(bits)]


def get_new_pixel(pixel, bits):
  return (
    set_lsb(pixel[0], bits),
    set_lsb(pixel[1], bits),
    set_lsb(pixel[2], bits)
  )

def hide(in_path, out_path, text):
  bits = get_bits(text)

  im = Image.open(in_path)
  print(os.path.basename(im.fp.name))
  print(os.path.dirname(im.fp.name))
  print(im.format, im.size, im.mode)

  pixelMap = im.load()
  img = Image.new(im.mode, im.size)
  pixelsNew = img.load()
  for i in range(img.size[0]):
    for j in range(img.size[1]):
      pixelMap[i,j] = get_new_pixel(pixelMap[i,j])

  img.show()
  im.close()
  img.close()


hide(sys.argv[1], sys.argv[2], sys.argv[3])
