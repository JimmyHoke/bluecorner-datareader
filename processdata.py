from PIL import Image, ImageColor
import pickle

# Make Heatmap

map = pickle.load(open("heatmap", "rb"))
img  = Image.new( mode = "RGB", size = (2000, 2000), color = (255, 255, 255))

maxheat = 0
for i in map:
    for j in i:
        if j > maxheat:
            maxheat = j

x = 0
for i in map:
    y = 0
    for j in i:
        heat = (j / maxheat) * 255
        if heat > 255:
            heat = 255
        diff = int(255 - heat * 500)
        diff2 = int(255 - heat * 1000)
        diff3 = int(255 - heat * 100)
        if diff < 0:
            diff = 0
        img.putpixel((x, y), (diff, diff2, diff3))
        y += 1
    x += 1

img.save('heatmap.png')

# Make Bluemap

map = pickle.load(open("bluemap", "rb"))
img  = Image.new( mode = "RGB", size = (2000, 2000), color = (255, 255, 255))

maxheat = 0
for i in map:
    for j in i:
        if j > maxheat:
            maxheat = j
x = 0
for i in map:
    y = 0
    for j in i:
        heat = (j / maxheat) * 255
        if heat > 255:
            heat = 255
        diff = int(255 - heat * 500)
        diff2 = int(255 - heat * 1000)
        diff3 = int(255 - heat * 100)
        if diff < 0:
            diff = 0
        img.putpixel((x, y), (diff, diff2, diff3))
        y += 1
    x += 1
img.save('bluemap.png')

# Find bluest pixel

bx = 0
by = 0
bv = 0

x = 0
for i in map:
    y = 0
    for j in i:
        if j >= 3:
            if j >= bv:
                bv = j
                bx = x
                by = y
        y += 1
    x += 1
print("Blue was placed at\tX: " + str(bx) + "\tY: " + str(by) + "\t" + str(bv) + " times.  More than anywhere else on the canvas.")

# Generate Nullmap

map = pickle.load(open("heatmap", "rb"))
img  = Image.new( mode = "RGB", size = (2000, 2000), color = (255, 255, 255))

zerocount = 0
x = 0
for i in map:
    y = 0
    for j in i:
        if j == 0:
            zerocount += 1
            img.putpixel((x, y), (0,0,0))
        y += 1
    x += 1
print('Tiles missing from dataset: ' + str(zerocount))
img.save('nullmap.png')
# Make Final Image

map = pickle.load(open("colormap", "rb"))
img  = Image.new( mode = "RGB", size = (2000, 2000), color = (255, 255, 255))

x = 0
for i in map:
    y = 0
    for j in i:
        if not (j == 0):
            img.putpixel((x, y), ImageColor.getrgb(j))
        y += 1
    x += 1

img.save('final-image-place-2022.png')

print('Done')