# Script that makes multiple HRD plots

#from classData import Data
from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np



# ------ Elements ------
def elements(model1, model2, model3, model4):

    # ------ Set Plot Style ------
    default_style()

    #if ms == True:
    # main sequence limit
    lim1 = model1.mainsequence()
    lim2 = model2.mainsequence()
    lim3 = model3.mainsequence()
    lim4 = model4.mainsequence()
    folder = 'MainSequence'
    # else:
    #     # full simulation
    #     lim1 = model1.end()
    #     lim2 = model2.end()
    #     lim3 = model3.end()
    #     lim4 = model4.end()
    #     folder = 'FullSimulation'

    # ------ Figure ------
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(9,6.5))
    
    #if ms == True:
    # fig.suptitle(f'Main Sequence: {mass}''M$_{\odot}$', fontweight='bold')
    # limit = '_ms'
    # else:
    #     fig.suptitle(f'Full Evolution: {mass}''M$_{\odot}$', fontweight='bold')
    #     limit = ''

    # ------ Plot 1 ------
    ax1.plot(model1.age[0:lim1], model1.lognh1[0:lim1], label = 'Vink 01', color = 'navy')
    ax1.plot(model2.age[0:lim2], model2.lognh1[0:lim2], label = 'Vink 18', color = 'darkred')
    ax1.plot(model3.age[0:lim3], model3.lognh1[0:lim3], label = 'Leuven', color = 'green')
    ax1.plot(model4.age[0:lim4], model4.lognh1[0:lim4], label = 'Krticka', color = 'pink')
    ax1.legend(shadow = False, edgecolor = 'k')
    ax1.set_xlabel('Age [Myr]')
    ax1.set_ylabel('log (H/H$_{\star}$)')
    ax1.set_title('Surface Hydrogen')
    #ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ Plot 2 ------
    ax2.plot(model1.age[0:lim1], model1.lognhe[0:lim1], label = 'Vink 01', color = 'navy')
    ax2.plot(model2.age[0:lim2], model2.lognhe[0:lim2], label = 'Vink 18', color = 'darkred')
    ax2.plot(model3.age[0:lim3], model3.lognhe[0:lim3], label = 'Leuven', color = 'green')
    ax2.plot(model4.age[0:lim4], model4.lognhe[0:lim4], label = 'Krticka', color = 'pink')
    ax2.set_xlabel('Age [Myr]')
    ax2.set_ylabel('log (He/He$_{\star}$)')
    ax2.set_title('Surface Helium')
    ax2.legend(shadow = False, edgecolor = 'k')

    # ------ Plot 3 ------
    ax3.plot(model1.age[0:lim1], model1.logncar[0:lim1], label = 'Vink 01', color = 'navy')
    ax3.plot(model2.age[0:lim2], model2.logncar[0:lim2], label = 'Vink 18', color = 'darkred')
    ax3.plot(model3.age[0:lim3], model3.logncar[0:lim3], label = 'Leuven', color = 'green')
    ax3.plot(model4.age[0:lim4], model4.logncar[0:lim4], label = 'Krticka', color = 'pink')
    ax3.legend(shadow = False, edgecolor = 'k')
    ax3.set_xlabel('Age [Myr]')
    ax3.set_ylabel('log (C/C$_{\star}$)')
    ax3.set_title('Surface Carbon')

    # ------ Plot 4 ------
    ax4.plot(model1.age[0:lim1], model1.lognnit[0:lim1], label = 'Vink 01', color = 'navy')
    ax4.plot(model2.age[0:lim2], model2.lognnit[0:lim2], label = 'Vink 18', color = 'darkred')
    ax4.plot(model3.age[0:lim3], model3.lognnit[0:lim3], label = 'Leuven', color = 'green')
    ax4.plot(model4.age[0:lim4], model4.lognnit[0:lim4], label = 'Krticka', color = 'pink')
    ax4.legend(shadow = False, edgecolor = 'k')
    ax4.set_xlabel('Age [Myr]')
    ax4.set_ylabel('log (N/N$_{\star}$)')
    ax4.set_title('Surface Nitrogen')
    
    plt.tight_layout()
    plt.show()
    #plt.savefig(f'Plots/{datafolder}/Subplots/Elements/{folder}/elem{mass}{limit}.png', dpi=200)

elements(mod1,mod2,mod3,mod4)