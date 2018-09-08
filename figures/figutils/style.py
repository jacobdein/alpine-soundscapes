"""
figutils.style
Helper functions to specify styles for figures.

Jacob Dein 2018
alpine-soundscapes
Author: Jacob Dein
License: MIT
"""

from matplotlib import rcParams

# set the font
def set_font():
    rcParams['font.sans-serif'] = ['Helvetica',
                                   'Arial',
                                   'Bitstream Vera Sans',
                                   'DejaVu Sans',
                                   'Lucida Grande',
                                   'Verdana',
                                   'Geneva',
                                   'Lucid',
                                   'Avant Garde',
                                   'sans-serif']
    
# create annotations with multiple leaders
def multi_annotate(ax, s, xy_list=[], *args, **kwargs):
    ans = []
    an = ax.annotate(s, xy_list[0], *args, **kwargs)
    ans.append(an)
    d = {}
    try:
        d['xycoords'] = kwargs['xycoords']
    except KeyError:
        pass
    try:
        d['arrowprops'] = kwargs['arrowprops']
    except KeyError:
        pass
    for xy in xy_list[1:]:
        an = ax.annotate(s, xy, alpha=0.0, xytext=(0,0), textcoords=an, **d)
        ans.append(an)
    return ans