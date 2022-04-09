# r/TheBlueCorner DataReader (Unofficial)

This set of tools reads the data from r/place (2022).

## Requirements

* python3
* Python Pillow Package (pip3 install pillow)
* You will need the place22-sorted-trimmed.csf file from [Here](https://jnfs.us-east-1.linodeobjects.com/place22-sorted-trimmed.csv).  Place it in your working directory along with the scripts.  (You could use another CSV file such as the original, but don't expect good results.)

## How to use

1. Install the dependencies listed above.
2. Run importdata.py.  This will read place22-sorted-trimmed.csv and convert it into a quickly readable format.
3. Run processdata.py.  This will generate a heatmap, bluemap, nullmap, and a final image

## Output

### Heatmap

A cool, custom heatmap that shows what areas had the most action.

### Bluemap

Like the heat map, but it only counts where blue (#2450A4) was placed

### Nullmap

These pixels are strangly missing from the dataset.  Weird.

### Final Image

This ain't your grandma's (or the Place admin's) final image.  This is the final image that has been r/TheBlueCorner Admin approved (ok it was just one admin but the point still stands).

### Console Output

Running importdata.py will output the number of missing tiles and the location of the tile that had blue placed on it the most.


LONG LIVE THE BLUE CORNER!
