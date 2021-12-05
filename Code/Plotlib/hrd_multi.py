# hrd_multi.py
#
# Functions for making a Hertzsprung Russel diagram of multiple models
#
# Freek Temming and Simon van Eeden

from .plotfunctions import *
import numpy as np
import matplotlib.pyplot as plt

SIGMA = 5.67051 * pow(10,-5)
R_SUN = 6.957 * pow(10,10)
L_SUN = 3.828 * pow(10,33)

def plot(models, save=False, custom_labels=None):
    """
    Creates Hertzsprung Russel diagram

    Input:
    model : mesaplot model
    """

    TITLE = f"Hertzsprung-Russel diagram"
    X_LABEL = 'log (T$_{\mathregular{eff}}$) [K]'
    Y_LABEL = 'log (L / L$_{\odot}$)'  
    CMAP = plt.get_cmap('cool')  

    # Make figure
    fig, ax = set_fig(TITLE, X_LABEL, Y_LABEL)

    # Evolutionary track per model
    for i, model in enumerate(models):
        # Main sequence
        row_start, row_end = get_main_sequence(model)
        x = model.hist.data['log_Teff'][row_start:row_end]
        y = model.hist.data['log_L'][row_start:row_end]

        # Labels
        if custom_labels:
            label = custom_labels[i]
        else:
            label = f"{model.hist.data['star_mass'][0]}" + "M$_{\odot}$"

        ax.plot(x, y, lw=2, label=label)

        # Whole track
        x = model.hist.data['log_Teff']
        y = model.hist.data['log_L']
        ax.plot(x, y, lw=2, color='k', alpha=0.2)

    # Lines of constant R
    set_const_R_lines(ax)

    # Legend
    ax.legend(shadow=False, edgecolor='white', fancybox=False)

    # Axis invert
    ax.invert_xaxis()

    # Show plot
    fig.tight_layout()
    plt.show()

    # Save
    if save:
        plt.savefig(f"Output/hrd_multi.png", dpi=200)


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


def set_const_R_lines(ax):
    """
    Creates lines of constant radius

    Input:
    ax : axis object
    """

    T_MIN = 3100
    T_MAX = 35000
    R_FRACTIONS = [0.01, 0.1, 1, 10, 100]

    for r_frac in R_FRACTIONS:

        luminosity = []
        temperature = []
       
        # Create line
        for T in [T_MIN, T_MAX]:

            L = 4 * np.pi * (r_frac*R_SUN)**2 * SIGMA * T**4
            luminosity.append(np.log10(L/L_SUN))
            temperature.append(np.log10(T))

        # Plot line
        ax.plot(
            temperature, 
            luminosity, 
            color='k',
            linestyle='--',
            linewidth=.5,
            alpha=0.7)

        # Text
        T=10000
        ax.text(            
            x=np.log10(T),
            y=np.log10((4 * np.pi * (r_frac*R_SUN)**2 * SIGMA * T**4)/L_SUN),
            s=f"{r_frac}" + "R$_{\odot}$",
            alpha=0.5)
