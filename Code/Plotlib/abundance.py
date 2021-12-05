# abundace.py
#
# Functions for plotting abundances over time
#
# Freek Temming and Simon van Eeden 

from .plotfunctions import *
import numpy as np
import matplotlib.pyplot as plt

def plot(model, elements):
    """
    Creates abundence of user input elements over time

    Input:
    model : mesaplot model
    """

    TITLE = f"{' '.join([str(elem) for elem in elements])} abundance"
    X_LABEL = 'Time'
    Y_LABEL = 'Mass Fraction' 
    ISOTOPES = {
        'H': 'center_h1',
        'He': 'center_he4',
        'C': 'center_c12',
        'N': 'center_n14',
        'O': 'center_o16'}

    # Make figure
    fig, ax = set_fig(TITLE, X_LABEL, Y_LABEL)

    # Abundance on main sequence
    row_start, row_end = get_main_sequence(model)
    x = model.hist.data['star_age'][row_start:row_end]
    for element in elements:
        ax.plot(
            x, 
            model.hist.data[f'{ISOTOPES[element]}'][row_start:row_end], 
            label=element) 

    # Legend
    ax.legend(shadow=False, edgecolor='white', fancybox=False)
    
    # Show
    plt.tight_layout()
    plt.show()
