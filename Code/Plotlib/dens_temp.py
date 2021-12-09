# dens_temp.py
#
# Functions for making a density temperature plot
#
# Freek Temming and Simon van Eeden 

from .plotfunctions import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, HPacker, VPacker

RHO_SUN = 1.41
T_SUN = 5778

def plot(model, save=False):
    """
    Creates density temperature plot

    Input:
    model : mesaplot model
    """

    TITLE = f"Central density vs central temperature {model.hist.data['star_mass'][0]}" + "M$_{\odot}$"
    X_LABEL = 'log ($\\rho$) [g cm$^{-3}$]'
    Y_LABEL = 'log (T) [K]'  

    # Make figure
    fig, ax = set_fig(TITLE, X_LABEL, Y_LABEL)

    # Equation of state regimes
    mu =  model.hist.data['center_mu'][0]
    mu_e =  model.hist.data['center_ye'][0]
    set_eos_regimes(ax, mu, mu_e)

    # Full track
    x = model.hist.data['log_cntr_Rho']
    y = model.hist.data['log_cntr_T']
    ax.plot(
        x, 
        y, 
        lw=1, 
        color='k', 
        alpha=.2)

    # Hydrogen core burning
    row_start, row_end = get_hydrogen_core_burning(model)
    ax.plot(
        x[row_start:row_end], 
        y[row_start:row_end], 
        lw=1, 
        color='green')

    # Helium core burning
    row_start, row_end = get_helium_core_burning(model)
    ax.plot(
        x[row_start:row_end], 
        y[row_start:row_end], 
        lw=1, 
        color='blue')

    multicolor_ylabel(ax,('Core hydrogen','Core helium'),('blue','green'), axis='yright', size=14, weight='bold')

    # Set margins around figure
    ax.margins(0, 0)

    fig.tight_layout()

    # Save
    if save:
        plt.savefig(f"../Output/dens_temp_{model.hist.data['star_mass'][0]}M.png", dpi=200)

    # Show
    plt.show()


def set_eos_regimes(ax, mu, mu_e):
    """
    Plot equation of state regimes
    """

    FACE_COLOR_BASE = 'red'
    LABEL_FONT_SIZE = 'small'
    rho_range = [-6, 9]  

    # Radiation
    temp_bot = [np.log10(rad_gas_eq(10**rho_range[0], mu)), np.log10(rad_gas_eq(10**rho_range[-1], mu))]
    temp_top = 11
    ax.fill_between(
        rho_range, 
        temp_bot, 
        temp_top, 
        facecolor=FACE_COLOR_BASE, 
        linewidth=0.0,
        alpha=0.1)
    ax.text(
        -5, 
        6.2, 
        'Radiation', 
        fontsize=LABEL_FONT_SIZE,
        color=FACE_COLOR_BASE,
        rotation=20)

    # Ideal gas
    rho_start = rho_range[0]
    rho_end = rho_range[-1]
    temp_top = [np.log10(rad_gas_eq(10**rho_start, mu)), np.log10(rad_gas_eq(10**rho_end, mu))]
    temp_bot = [np.log10(gas_NR_eq(10**rho_start, mu, mu_e)), np.log10(gas_NR_eq(10**rho_end, mu, mu_e))]
    ax.fill_between(
        [rho_start, rho_end], 
        temp_bot, 
        temp_top, 
        facecolor=FACE_COLOR_BASE, 
        linewidth=0.0,
        alpha=0,
        label='ND')
    ax.text(
        -5, 
        2.2, 
        'Ideal gas', 
        fontsize=LABEL_FONT_SIZE,
        color=FACE_COLOR_BASE,
        rotation=37)
   
    # Electron degeneray 
    rho_start = rho_range[0]
    rho_end = np.log10(NR_R_eq(mu_e))
    temp_top = [np.log10(gas_NR_eq(10**rho_start, mu, mu_e)), np.log10(gas_NR_eq(10**rho_end, mu, mu_e))]
    temp_bot = temp_top[0]
    ax.fill_between(
        [rho_start, rho_end], 
        temp_bot, 
        temp_top, 
        facecolor=FACE_COLOR_BASE, 
        linewidth=0.0,
        alpha=0.07,
        label='ND')
    ax.text(
        -3.2, 
        2.2, 
        'Electron degeneracy', 
        fontsize=LABEL_FONT_SIZE,
        color=FACE_COLOR_BASE,
        rotation=37)

    # Relativistic
    rho_start = np.log10(NR_R_eq(mu_e))
    rho_R_ER = np.log10(R_ER_eq(mu_e))
    rho_end = rho_range[-1]
    temp_top = [np.log10(gas_NR_eq(10**rho_start, mu, mu_e)), np.log10(gas_ER_eq(10**rho_R_ER, mu, mu_e)), np.log10(gas_ER_eq(10**rho_end, mu, mu_e))]
    temp_bot = np.log10(gas_NR_eq(10**rho_range[0], mu, mu_e))
    ax.fill_between(
        [rho_start, rho_R_ER ,rho_end], 
        temp_bot, 
        temp_top, 
        facecolor=FACE_COLOR_BASE, 
        linewidth=0.0,
        alpha=0.15,
        label='Relativistic')
    ax.text(
        6.4, 
        8.7, 
        'Relativistic', 
        fontsize=LABEL_FONT_SIZE,
        color=FACE_COLOR_BASE,
        rotation=20)


def rad_gas_eq(rho, mu):
    """
    Radiation pressure equals ideal gas

    Return:
    temperature
    """

    return 3.2 * 10**7 * mu**(-1/3) * rho**(1/3)


def gas_NR_eq(rho, mu, mu_e):
    """
    Ideal gas pressure equals non relativistic electron degeneracy pressure

    Return:
    temperature
    """

    return 1.21 * 10**5 * mu * mu_e**(-5/3) * rho**(2/3)


def NR_R_eq(mu_e):
    """
    Relativistic pressure equals non relativistic pressure

    Return:
    density
    """

    return 9.7 * 10**5 * mu_e


def gas_ER_eq(rho, mu, mu_e):
    """
    Ideal gas pressure equals extremely relativistic degeneracy pressure

    Return:
    temperature
    """

    return 1.50 * 10**7 * mu * mu_e**(-4/3) * rho**(1/3)


def R_ER_eq(mu_e):
    """
    Relativistic pressure equals extremely relativistic pressure

    Return:
    density
    """

    return ((1.50 * 10**7)/(1.21 * 10**5))**3 * mu_e


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

