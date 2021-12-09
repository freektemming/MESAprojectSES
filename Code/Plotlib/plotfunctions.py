from .plotstyles import *

def set_fig(title, x_label, y_label):
    """
    Creates figure and axis, with title and labels

    Input:
    title
    x_label
    y_label
    """

    default_style()

    fig, ax = plt.subplots(1,1)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    return fig, ax


def get_main_sequence(model):
    """
    Get rows starting from the main sequence

    Input:
    model : mesaplot
    """

    index = 0
    for log_L, log_Lnuc in zip(model.hist.data['log_L'], model.hist.data['log_Lnuc']):

        # # When luminosity increases the main sequence will start
        # if h1 < 0.69:
        #     return index, -1

        # When luminosity is dominates by nuclear fusion
        if (10**log_Lnuc)/(10**log_L) > 0.99:
            return index, -1

        index += 1

    return 0, -1

def get_helium_burning_phase(model):
    """
    Get rows starting from the helium burning phase

    Input:
    model : mesaplot
    """

    index = 0
    for center_h in model.hist.data['center_h1']:

        # When hydrogen is burned up in the core
        if center_h < 0.01:
            for center_he in model.hist.data['center_he4'][index:-1]:
                if center_he < 0.98:
                    return index, -1

        index += 1