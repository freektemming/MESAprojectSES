# dens_temp.py
#
# Functions for making a density temperature plot
#
# Freek Temming and Simon van Eeden 

from .plotfunctions import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

RHO_SUN = 1.41
T_SUN = 5778

def plot(model, save=False):
    """
    Creates density temperature plot

    Input:
    model : mesaplot model
    """

    TITLE = f"Central density vs central temperature {model.hist.data['star_mass'][0]}" + "M$_{\odot}$"
    X_LABEL = 'log ($\\rho$)'
    Y_LABEL = 'log (T)'  
    CMAP = plt.get_cmap('cool')  

    # Make figure
    fig, ax = set_fig(TITLE, X_LABEL, Y_LABEL)

    # Gradient line
    row_start, row_end = get_main_sequence(model)
    x = model.hist.data['log_cntr_Rho'][row_start:row_end]
    y = model.hist.data['log_cntr_T'][row_start:row_end]
    age = model.hist.data['star_age'][row_start:row_end] / 1000000 # Convert to mega year
    line = set_grad_line(ax, x, y, age, CMAP)

    # Equation of state regimes
    mu =  model.hist.data['center_mu'][0]
    mu_e =  model.hist.data['center_ye'][0]
    set_eos_regimes(ax, mu, mu_e)

    # Colorbar
    cbar = fig.colorbar(
        line,
        cmap=CMAP,
        ax=ax)
    cbar.set_label('Age [Myr]')

    # Set margins around figure
    ax.margins(0, 0)

    # Show plot
    fig.tight_layout()
    plt.show()

    # Save
    if save:
        plt.savefig(f"Output/dens_temp_{model.hist.data['star_mass'][0]}M", dpi=200)


def set_grad_line(ax, x, y, cmap_vals, cmap):
    """
    Plot gradient line
    """

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(
            segments, 
            cmap=cmap,
            norm=plt.Normalize(min(cmap_vals), max(cmap_vals)))

    # Assign each line segment to a color
    lc.set_array(cmap_vals)

    # Set line widht
    lc.set_linewidth(3)

    # Add linesegments to axis
    line = ax.add_collection(lc)

    return line


def set_eos_regimes(ax, mu, mu_e):
    """
    Plot equation of state regimes
    """

    FACE_COLOR_BASE = 'red'
    LABEL_FONT_SIZE = 'small'
    rho_range = [.6, 7.2]  

    # Radiation
    temp_bot = [np.log10(rad_gas_eq(10**rho_range[0], mu)), np.log10(rad_gas_eq(10**rho_range[-1], mu))]
    temp_top = temp_bot[-1]
    ax.fill_between(
        rho_range, 
        temp_bot, 
        temp_top, 
        facecolor=FACE_COLOR_BASE, 
        linewidth=0.0,
        alpha=0.1)
    ax.text(
        1, 
        8.2, 
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
        1, 
        6, 
        'Ideal gas', 
        fontsize=LABEL_FONT_SIZE,
        color=FACE_COLOR_BASE,
        rotation=40)
   
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
        2.1, 
        6, 
        'Electron degeneracy', 
        fontsize=LABEL_FONT_SIZE,
        color=FACE_COLOR_BASE,
        rotation=40)

    # Relativistic
    rho_start = np.log10(NR_R_eq(mu_e))
    rho_end = rho_range[-1]
    temp_top = [np.log10(gas_NR_eq(10**rho_start, mu, mu_e)), np.log10(gas_NR_eq(10**rho_end, mu, mu_e))]
    temp_bot = np.log10(gas_NR_eq(10**rho_range[0], mu, mu_e))
    ax.fill_between(
        [rho_start, rho_end], 
        temp_bot, 
        temp_top, 
        facecolor=FACE_COLOR_BASE, 
        linewidth=0.0,
        alpha=0.15,
        label='Relativistic')
    ax.text(
        6.1, 
        8.7, 
        'Relativistic', 
        fontsize=LABEL_FONT_SIZE,
        color=FACE_COLOR_BASE,
        rotation=40)


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

