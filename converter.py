from PIL import Image
import sys

try: filename = sys.argv[1]
except IndexError:
    print("usage: ./converter.py <image>")
    filename = "image.png"

image = Image.open(filename)
image = image.convert("1")
pixelmap = image.load()


from semigraphics import braille
for j in range(0, 32, 7):
    for i in range(0, 88, 2):
        x = tuple([
            tuple([bool(pixelmap[i+0,j+0]), bool(pixelmap[i+1,j+0])]),
            tuple([bool(pixelmap[i+0,j+1]), bool(pixelmap[i+1,j+1])]),
            tuple([bool(pixelmap[i+0,j+2]), bool(pixelmap[i+1,j+2])]),
            tuple([bool(pixelmap[i+0,j+3]), bool(pixelmap[i+1,j+3])])
        ])
        print(braille[x], end='')
    print()