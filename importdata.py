import pickle


# Generate Maps

file1 = open('place22-sorted-trimmed.csv', 'r')
heatmap = [[0 for i in range(2000)] for j in range(2000)]
bluemap = [[0 for i in range(2000)] for j in range(2000)]
colormap = [[0 for i in range(2000)] for j in range(2000)]
line = 0

for i in heatmap:
    for j in i:
        j = 0

for i in bluemap:
    for j in i:
        j = 0

while 1:
    nextline = file1.readline().removesuffix('\n')
    if not nextline:
        break
    ld = nextline.split(',')
    if not (len(ld) == 4):
        x = int(ld[3].removeprefix('"'))
        y = int(ld[4].removesuffix('"'))
        color = ld[2]
        heatmap[x][y] += 1
        if color == '#2450A4':
            bluemap[x][y] += 1
        colormap[x][y] = color
        line += 1
        print((line/155915946) * 100)
pickle.dump(heatmap, open("heatmap", "wb"))
pickle.dump(bluemap, open("bluemap", "wb"))
pickle.dump(colormap, open("colormap", "wb"))