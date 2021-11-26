# Script that makes multiple HRD plots

#from classData import Data
from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# ------ plot normal HRD 1 Model, All Masses------
def hrd(model1, model2, model3, model4, model5):

    # limits

    # main sequence limit
    lim1 = model1.mainsequence()
    lim2 = model2.mainsequence()
    lim3 = model3.mainsequence()
    lim4 = model4.mainsequence()
    lim5 = model5.mainsequence()

    # age limit colorbar
    min1 = model1.get_min_bar()
    max1 = model1.get_age(lim1)

    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = HRD('test')

    # plot line
    ax.plot(model1.Teff[0:lim1], model1.logL[0:lim1], lw = 1, color = 'black')
    ax.plot(model2.Teff[0:lim2], model2.logL[0:lim2], lw = 1, color = 'black')
    ax.plot(model3.Teff[0:lim3], model3.logL[0:lim3], lw = 1, color = 'black')
    ax.plot(model4.Teff[0:lim4], model4.logL[0:lim4], lw = 1, color = 'black')
    ax.plot(model5.Teff[0:lim5], model5.logL[0:lim5], lw = 1, color = 'black')

    # plot colors
    ims1 = ax.scatter(model1.Teff[0:lim1], model1.logL[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims2 = ax.scatter(model2.Teff[0:lim2], model2.logL[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims3 = ax.scatter(model3.Teff[0:lim3], model3.logL[0:lim3], c= model3.age[0:lim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims4 = ax.scatter(model4.Teff[0:lim4], model4.logL[0:lim4], c= model4.age[0:lim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims5 = ax.scatter(model5.Teff[0:lim5], model5.logL[0:lim5], c= model5.age[0:lim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    #ax.legend(shadow = False, edgecolor = 'k')

    # ------ Text ------
    ax.text(model1.Teff[0] + 5, model1.logL[0], '20M$_{\odot}$', fontweight = 'bold')
    ax.text(model2.Teff[0] + 5, model2.logL[0], '30M$_{\odot}$', fontweight = 'bold')
    ax.text(model3.Teff[0] + 5, model3.logL[0], '40M$_{\odot}$', fontweight = 'bold')
    ax.text(model4.Teff[0] + 5, model4.logL[0], '50M$_{\odot}$', fontweight = 'bold')
    ax.text(model5.Teff[0] + 5, model5.logL[0], '60M$_{\odot}$', fontweight = 'bold')
    
    fig.tight_layout()
    plt.show()
    #plt.savefig(f'Plots/{datafolder}/HRDmodels/{folder}/HRD{number}{limit}.png', dpi=200)

hrd(mod1,mod2,mod3,mod4,mod5)