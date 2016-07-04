# alpine-soundscapes
A collection of scripts and [jupyter](http://jupyter.org) notebooks to analyze soundscapes — developed from my "Soundscapes of the Alpine Landscapes" project in Innsbruck, Austria supported by a Fulbright U.S. Grant.

## Setup

### GRASS
Some of the notebooks use [GRASS GIS](https://grass.osgeo.org) (7.0.4), and must be run inside of a GRASS environment (start the jupyter notebook server from the GRASS command line).

Setup GRASS with a new location and mapset using an [EPSG](http://spatialreference.org) code:
```Shell
$ grass -c EPSG:31254 /home/ubuntu/grassdata/Innsbruck/PERMANENT
```

From the GRASS command line, disable the GUI:
```
GRASS:~ > g.gisenv set=GRASS_GUI=text
```

From the GRASS command line, start the jupyter notebook server:
```
GRASS:~ > jupyter notebook
```

![screenshot - starting jupyter notebook](/images/screenshots/starting-jupyter-notebook.png)
