# script to plot kippenhahn diagrams

from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.ticker import FormatStrFormatter 
from matplotlib.collections import LineCollection
import numpy as np
import math
from pylab import *


#------ Constants ------
sigma = 5.67051 * pow(10,-5)  # cgs
Rsun = 6.957 * pow(10,10)
Lsun = 3.828 * pow(10,33)
Msun = 1.99 * pow(10,33)
pi = np.pi

# ----- Function to Plot Labels on Axis
def multicolor_ylabel(ax,list_of_strings,list_of_colors,axis='x',anchorpad=0,**kw):
    """this function creates axes labels with multiple colors
    ax specifies the axes object where the labels should be drawn
    list_of_strings is a list of all of the text items
    list_if_colors is a corresponding list of colors for the strings
    axis='x', 'y', or 'both' and specifies which label(s) should be drawn"""
    from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, HPacker, VPacker

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
        anchored_ybox = AnchoredOffsetbox(loc=3, child=ybox, pad=anchorpad, frameon=False, bbox_to_anchor=(1.1, 0.05), 
                                        bbox_transform=ax.transAxes, borderpad=0.)
        ax.add_artist(anchored_ybox)


# ------ Mass Fractions and Convection ------
def kip(model, mass, ms):

    if ms == True:
        # main sequence limit
        lim = model.mainsequence()
        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        lim = len(model.age)
        limit = ''
        folder = 'FullSimulation'

    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = kippenhahn(mass)

    # list for x-axis structure plot
    # baseZ = zams.age()
    # baseM = mid.age()
    # baseT = tams.age()

    # BaseZams = [baseZ] * len(zams.normR)
    # BaseMid = [baseM] * len(mid.normR)
    # BaseTams = [baseT] * len(tams.normR)
    
    # ------ Plot Lines ------
    ax.plot(model.time[0:lim], model.ntoth1[0:lim], color = 'deeppink', label = 'Hydrogen')
    ax.plot(model.time[0:lim], model.ntothe[0:lim], color = 'darkred', label = 'Helium')
    ax.plot(model.time[0:lim], model.ntotc[0:lim], color = 'blue', label = 'Carbon')
    
    # ------ Plot Colors ------
    # ims1 = ax.scatter(BaseZams, zams.normM * model.nmass[zams.model() - model.x], c= zams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 6, zorder = 2)
    # ims2 = ax.scatter(BaseMid, mid.normM * model.nmass[mid.model() - model.x], c= mid.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 6, zorder = 2)
    # ims3 = ax.scatter(BaseTams, tams.normM * model.nmass[tams.model() - model.x], c= tams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 6, zorder = 2)
    # cbar1 = fig.colorbar(ims1, ax = ax)
    # cbar1.set_label('Zones')

    # ------ Fill Planes ------
    ax.fill_between(model.time[0:lim], model.convtop[0:lim], model.nmass[0:lim], alpha = 0.5, color = 'grey', hatch = '///')
    ax.fill_between(model.time[0:lim], 0, model.convective_core[0:lim], alpha = 0.2, color = 'grey', hatch = '///')

    # ------ Text ------
    ax.text(1.3, 0.2, 'Convective core', fontweight = 'bold')
    ax.text(1, 0.8, 'Radiative envelope', fontweight = 'bold')

    # ------ Plot Colors On Axis ------
    multicolor_ylabel(ax,('Hydrogen','Helium','Carbon'),('blue','darkred','deeppink'),axis='yleft',size=14,weight='bold')
    #multicolor_ylabel(ax,('Convection','Overshoot','Radiation'),('lightblue','seagreen','navy'),axis='yright',size=14,weight='bold')

    # ------ Show ------
    #plt.legend(shadow = False, edgecolor = 'k')
    fig.tight_layout()
    plt.show()

    #plt.savefig(f'Plots/{datafolder}/Kippenhahn/{folder}/Kip{number}_{mass}{limit}.png')

kip(mod1,20,False)