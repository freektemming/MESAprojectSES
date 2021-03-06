# kip.py
#
# Functions for making a kippenhahn diagram
#
# Freek Temming and Simon van Eeden 

from .plotfunctions import *
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.ticker import FormatStrFormatter 
from matplotlib.collections import LineCollection
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, HPacker, VPacker
import numpy as np
import math
from pylab import *

SIGMA = 5.67051 * pow(10,-5)
R_SUN = 6.957 * pow(10,10)
L_SUN = 3.828 * pow(10,33)
M_SUN = 1.99 * pow(10,33)
pi = np.pi

def plot(model, save=False):
    """
    Creates Kippenhahn diagram

    Input:
    model : mesaplot model
    """

    mass = model.hist.data['star_mass'][0]
    TITLE = f'Kippenhahn {mass}M''$_{\odot}$'
    X_LABEL = 'Model Number'
    Y_LABEL = 'm / M$_{\star}$'  
    CMAP = plt.get_cmap('cool')  

    # Make figure
    fig, ax = set_fig(TITLE, X_LABEL, Y_LABEL)

    # Full track starting at main sequence
    row_start, row_end = get_main_sequence(model)
    row_end = -1
   
    # colormap = plt.cm.cividis_r
    colormap = plt.cm.cubehelix

    # ax.set_xticks([0.0648,3.12,4.76])
    # ax.set_xticklabels(['Zams', 'Mid','Tams'])
        
    # age = model.hist.data['star_age']/1000000 # Time axis in M years
    age = model.hist.data['model_number'] # Time axis in model number
    hydrogen = model.hist.data['center_h1']
    helium = model.hist.data['center_he4']
    carbon = model.hist.data['center_c12']
    ax.plot(age[row_start:row_end], hydrogen[row_start:row_end], color = 'red', label = 'Hydrogen')
    ax.plot(age[row_start:row_end], helium[row_start:row_end], color = 'green', label = 'Helium')
    ax.plot(age[row_start:row_end], carbon[row_start:row_end], color = 'blue', label = 'Carbon')
    
    # Convective regions
    ax.fill_between(
        age[row_start:row_end], 
        model.hist.data['conv_mx1_top'][row_start:row_end], 
        model.hist.data['conv_mx1_bot'][row_start:row_end], 
        facecolor="gainsboro", 
        linewidth=0.0)
    ax.fill_between(
        age[row_start:row_end], 
        model.hist.data['conv_mx2_top'][row_start:row_end], 
        model.hist.data['conv_mx2_bot'][row_start:row_end], 
        facecolor="gainsboro",  
        linewidth=0.0)

    # Convective core
    conv_core_mass_norm = model.hist.data['mass_conv_core'][row_start:row_end]/model.hist.data['star_mass'][row_start:row_end]
    ax.fill_between(
        age[row_start:row_end], 
        0, 
        conv_core_mass_norm, 
        facecolor="gainsboro", 
        linewidth=0.0)

    # Active burning regions
    plt.rcParams['hatch.color'] = 'k'
    plt.rcParams['hatch.linewidth'] = 0.5
    ax.fill_between(
        age[row_start:row_end], 
        model.hist.data['epsnuc_M_1'][row_start:row_end]/(model.hist.data['star_mass'][row_start:row_end] * M_SUN), 
        model.hist.data['epsnuc_M_4'][row_start:row_end]/(model.hist.data['star_mass'][row_start:row_end] * M_SUN), 
        alpha=0.1,
        color="red",
        hatch="",
        linewidth=0.0)

    ax.fill_between(
        age[row_start:row_end], 
        model.hist.data['epsnuc_M_5'][row_start:row_end]/(model.hist.data['star_mass'][row_start:row_end] * M_SUN), 
        model.hist.data['epsnuc_M_8'][row_start:row_end]/(model.hist.data['star_mass'][row_start:row_end] * M_SUN), 
        alpha=0.1,
        color='red',
        hatch="",
        linewidth=0.0)
    
    # Plot labels around axis
    multicolor_ylabel(ax, ('Hydrogen','Helium','Carbon'),('blue','green','red'), axis='yleft', size=14, weight='bold')
    # multicolor_ylabel(ax,('Convection','Overshoot','Radiation'),('lightblue','seagreen','navy'),axis='yright',size=14,weight='bold')
    multicolor_ylabel(ax,('Convective region','Nuclear burning'),('salmon','gray'), axis='yright', size=14, weight='bold')

    fig.tight_layout()

    # Save
    if save:
        plt.savefig(f'../Output/Kippenhahn_{mass}M.png', dpi=200)

    # Show
    plt.show()


def multicolor_ylabel(ax, list_of_strings, list_of_colors, axis='x', anchorpad=0, **kw):
    """this function creates axes labels with multiple colors
    ax specifies the axes object where the labels should be drawn
    list_of_strings is a list of all of the text items
    list_if_colors is a corresponding list of colors for the strings
    axis='x', 'y', or 'both' and specifies which label(s) should be drawn"""

    # x-axis label
    if axis=='x' or axis=='both':
        boxes = [TextArea(text, textprops=dict(color=color, ha='left',va='bottom',**kw)) 
                    for text,color in zip(list_of_strings,list_of_colors) ]
        xbox = HPacker(children=boxes,align="center",pad=0, sep=5)
        anchored_xbox = AnchoredOffsetbox(loc=3, child=xbox, pad=anchorpad,frameon=False,bbox_to_anchor=(0.2, -0.09),
                                        bbox_transform=ax.transAxes, borderpad=0.)
        ax.add_artist(anchored_xbox)

    # y-axis label
    if axis=='yleft' or axis=='both':
        boxes = [TextArea(text, textprops=dict(color=color, ha='left',va='bottom',rotation=90,**kw)) 
                    for text,color in zip(list_of_strings[::-1],list_of_colors) ]
        ybox = VPacker(children=boxes,align="center", pad=0, sep=50)
        anchored_ybox = AnchoredOffsetbox(loc=3, child=ybox, pad=anchorpad, frameon=False, bbox_to_anchor=(-.20, 0.05), 
                                        bbox_transform=ax.transAxes, borderpad=0.)
        ax.add_artist(anchored_ybox)
    
    # y-axis label
    if axis=='yright' or axis=='both':
        boxes = [TextArea(text, textprops=dict(color=color, ha='left',va='bottom',rotation=90,**kw)) 
                    for text,color in zip(list_of_strings[::-1],list_of_colors) ]
        ybox = VPacker(children=boxes,align="center", pad=0, sep=30)
        anchored_ybox = AnchoredOffsetbox(loc=3, child=ybox, pad=anchorpad, frameon=False, bbox_to_anchor=(1.05, 0.05), 
                                        bbox_transform=ax.transAxes, borderpad=0.)
        ax.add_artist(anchored_ybox)