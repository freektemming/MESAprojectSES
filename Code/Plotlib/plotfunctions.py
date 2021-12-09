from .plotstyles import *

def set_fig(title, x_label, y_label):
    """
    Creates figure and axis, with title and labels

    Input:
    title
    x_label
    y_label

    Return:
    (figure, axis)
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

    Return:
    (row_start, row_end)
    """

    # Start
    index = 0
    for log_L, log_Lnuc in zip(model.hist.data['log_L'], model.hist.data['log_Lnuc']):
        # When luminosity is dominates by nuclear fusion
        if (10**log_Lnuc)/(10**log_L) > 0.99:
            row_start = index
            break

        index += 1

    # End
    index = 0
    for center_h1 in model.hist.data['center_h1']:
        # When hydrogen is burned up
        if center_h1 < 0.001:
            row_end = index
            break

        index += 1

    return row_start, row_end


def get_hydrogen_core_burning(model):
    """
    Get rows containing hydrogen core burning phase

    Input:
    model : mesaplot

    Return:
    (row_start, row_end)
    """

    row_start_MS, row_end_MS = get_main_sequence(model)

    index = 0
    for center_h in model.hist.data['center_h1']:

        # When hydrogen is burned up in the core
        if center_h < 0.01: 
            return row_start_MS, index

        index += 1


def get_helium_core_burning(model):
    """
    Get rows starting from the helium core burning phase

    Input:
    model : mesaplot

    Return:
    (row_start, row_end)
    """

    index = 0
    for center_h in model.hist.data['center_h1']:

        # When hydrogen is burned up in the core
        if center_h < 0.01:
            for center_he in model.hist.data['center_he4'][index:-1]:
                if center_he < 0.97:
                    return index, -1

                index += 1

        index += 1