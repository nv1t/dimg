import Image
import sys
import math,operator
import os

filename=sys.argv[1]

size = int(math.ceil(math.sqrt(int(os.path.getsize(filename))/3)))
img = Image.new("RGB", (size,size),"black")
pixels = img.load()

f = open(filename,'rb')
for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
	b = [ord(x) if x else 255 for x in f.read(3)] + [255]*3
	pixels[j,i] = (b[0],b[1],b[2])

img.save(sys.stdout,"PNG")
