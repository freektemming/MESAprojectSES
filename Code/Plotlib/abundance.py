# abundace.py
#
# Functions for plotting abundances over time
#
# Freek Temming and Simon van Eeden 

from .plotfunctions import *
import numpy as np
import matplotlib.pyplot as plt

def plot(model, elements, zoom=False, save=False):
    """
    Creates abundence of user input elements over time

    Input:
    model : mesaplot model
    """

    TITLE = f"{', '.join([str(elem) for elem in elements])} abundance"
    X_LABEL = 'Time [Myr]'
    Y_LABEL = 'Mass Fraction [m/M$_{\star}$]' 
    ISOTOPES = {
        'H': 'center_h1',
        'He': 'center_he4',
        'C': 'center_c12',
        'N': 'center_n14',
        'O': 'center_o16'}

    # Make figure
    fig, ax = set_fig(TITLE, X_LABEL, Y_LABEL)
    
    # Abundance on helium core burning phase
    if zoom == True:
        row_start, row_end = get_helium_core_burning(model)
    # Abundance on main sequence
    else:
        row_start, row_end = get_main_sequence(model)

    x = model.hist.data['star_age'][row_start:row_end] / 1000000 #HARDCODE
    for element in elements:
        ax.plot(
            x, 
            model.hist.data[ISOTOPES[element]][row_start:row_end], 
            label=element) 

    # Legend
    ax.legend(shadow=False, edgecolor='white', fancybox=False, fontsize="small", facecolor='none')
    
    plt.tight_layout()

    if save:
        plt.savefig(f"../Output/abundance_{'-'.join([str(elem) for elem in elements])}_{model.hist.data['star_mass'][0]}M.png", dpi=200)

    # Show
    plt.show()
