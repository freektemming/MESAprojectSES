# Script that makes multiple HRD plots

#from classData import Data
from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import math

# ------ plot normal HRD 1 Model, All Masses------
def hrdplot(model1):


    # main sequence limit
    lim1 = -1
    # lim2 = model2.mainsequence()
    # lim3 = model3.mainsequence()
    # lim4 = model4.mainsequence()
    # lim5 = model5.mainsequence()

    # age limit colorbar
    min1 = model1.hist.data['star_age'][0]
    max1 = model1.hist.data['star_age'][-1]

    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = HRD('test')

    # compute at constant radius
    sigma = 5.67051 * pow(10,-5)
    R_sun = 6.957 * pow(10,10)
    L_sun = 3.828 * pow(10,33)

    for fraction in [0.01,0.1,1,10,100]:

        luminosity = []
        temperature = []
        
        for T in range(0,30000,100):

            L = 4 * math.pi * sigma * T**4 * fraction*R_sun**2
            luminosity.append(np.log10(L/L_sun))
            temperature.append(np.log10(T))
        ax.plot(temperature,luminosity)


    # plot line
    ax.plot(model1.hist.data['log_Teff'], model1.hist.data['log_L'], lw = 1, color = 'black')
    # ax.plot(model2.Teff[0:lim2], model2.logL[0:lim2], lw = 1, color = 'black')
    # ax.plot(model3.Teff[0:lim3], model3.logL[0:lim3], lw = 1, color = 'black')
    # ax.plot(model4.Teff[0:lim4], model4.logL[0:lim4], lw = 1, color = 'black')
    # ax.plot(model5.Teff[0:lim5], model5.logL[0:lim5], lw = 1, color = 'black')
    ax.plot(temperature,luminosity)

    # plot colors
    ims1 = ax.scatter(model1.hist.data['log_Teff'], model1.hist.data['log_L'], c= model1.hist.data['star_age'], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    # ims2 = ax.scatter(model2.Teff[0:lim2], model2.logL[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    # ims3 = ax.scatter(model3.Teff[0:lim3], model3.logL[0:lim3], c= model3.age[0:lim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    # ims4 = ax.scatter(model4.Teff[0:lim4], model4.logL[0:lim4], c= model4.age[0:lim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    # ims5 = ax.scatter(model5.Teff[0:lim5], model5.logL[0:lim5], c= model5.age[0:lim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    #ax.legend(shadow = False, edgecolor = 'k')

    # ------ Text ------
    # ax.text(model1.Teff[0] + 5, model1.logL[0], '20M$_{\odot}$', fontweight = 'bold')
    # ax.text(model2.Teff[0] + 5, model2.logL[0], '30M$_{\odot}$', fontweight = 'bold')
    # ax.text(model3.Teff[0] + 5, model3.logL[0], '40M$_{\odot}$', fontweight = 'bold')
    # ax.text(model4.Teff[0] + 5, model4.logL[0], '50M$_{\odot}$', fontweight = 'bold')
    # ax.text(model5.Teff[0] + 5, model5.logL[0], '60M$_{\odot}$', fontweight = 'bold')
    
    fig.tight_layout()
    plt.show()
    #plt.savefig(f'Plots/{datafolder}/HRDmodels/{folder}/HRD{number}{limit}.png', dpi=200)

