# alpine-soundscapes
A collection of [jupyter](http://jupyter.org) notebooks for analyzing soundscapes — developed from my "Soundscapes of the Alpine Landscapes" project in Innsbruck, Austria supported by a Fulbright U.S. student grant.

## Maps

A main goal of the project is to map the soundscape across the landscape. Here is a [map](https://jacobdein.github.io/alpine-soundscapes/) of biophony over the landscape near the study area. The map is based on an early version of a multilevel regression [model](https://github.com/jacobdein/alpine-soundscapes/blob/master/Regression%20model.ipynb) developed from data collected in the field.

## Mission

We am currently revising, improving, and adding new notebooks as we wrap up the project. All the data and results used in the analyses will be made easily accessible in the near future. We have tried to document my analysis process well and hope that this information will be useful to further soundscape research. We welcome suggestions and comments!

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
