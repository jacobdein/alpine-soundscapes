"""
figutils.query
Helper functions to query data for figures.

Jacob Dein 2018
alpine-soundscapes
Author: Jacob Dein
License: MIT
"""

import geopandas
import pyproj
import gdal
from django.db import connection
from landscape.models import LandCover
from django.contrib.gis.db.models.functions import Intersection, Envelope

# define the coordinate system
austria_mgd = pyproj.Proj(init='epsg:31254')

# query database using geopandas
def get_geodataframe(queryset, modification=None, crs=austria_mgd):
    query = queryset.query.sql_with_params()
    if modification:
        query = (modification, query[1])
    return geopandas.read_postgis(query[0], connection, 
                                   geom_col='geometry', 
                                   params=query[1], 
                                   index_col='id',
                                   crs=crs)

# query database for land cover around a point within a specified radius
def get_landcover(point, radius=100):
    buffer = point.buffer(radius)
    result = LandCover.objects.filter(geometry__intersects=buffer.envelope)\
                          .annotate(intersection=Intersection('geometry', buffer.envelope))
    return result

# query database for a raster to be returned as a NumPy array
def get_raster(query):
    cursor = connection.cursor()
    cursor.execute(sql=query)
    vsipath = '/vsimem/from_postgis'
    memview = cursor.fetchone()[0]
    gdal.FileFromMemBuffer(vsipath, bytes(memview))
    ds = gdal.Open(vsipath)
    band = ds.GetRasterBand(1)
    data = band.ReadAsArray()
    ds = band = None
    gdal.Unlink(vsipath)
    return data