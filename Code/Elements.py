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
def HHE(model1, model2, model3, model4):

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
    fig, ax = plt.subplots(1,1)

    ax.set_xlabel('Time')
    ax.set_ylabel('Mass Fraction')
    ax.set_title(f'Central H and He')
    
    #if ms == True:
    # fig.suptitle(f'Main Sequence: {mass}''M$_{\odot}$', fontweight='bold')
    # limit = '_ms'
    # else:
    #     fig.suptitle(f'Full Evolution: {mass}''M$_{\odot}$', fontweight='bold')
    #     limit = ''

    # ------ Plot 1 ------
    ax.plot(model1.age[0:lim1], model1.HC[0:lim1], label = 'Hydrogen', color = 'navy')
    ax.plot(model2.age[0:lim2], model2.HeC[0:lim2], label = 'Helium', color = 'darkred')
    # ax.plot(model3.age[0:lim3], model3.lognh1[0:lim3], label = 'Leuven', color = 'green')
    # ax.plot(model4.age[0:lim4], model4.lognh1[0:lim4], label = 'Krticka', color = 'pink')
    ax.legend(shadow = False, edgecolor = 'k')
    # ax.set_xlabel('Age [Myr]')
    # ax.set_ylabel('log (H/H$_{\star}$)')
    # ax.set_title('Surface Hydrogen')
    #ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    
    plt.tight_layout()
    plt.show()
    #plt.savefig(f'Plots/{datafolder}/Subplots/Elements/{folder}/elem{mass}{limit}.png', dpi=200)

HHE(mod1,mod2,mod3,mod4)

# ------ Elements ------
def CNO(model1, model2, model3, model4):

    # ------ Set Plot Style ------
    default_style()

    #if ms == True:
    # main sequence limit
    # lim1 = model1.mainsequence()
    # lim2 = model2.mainsequence()
    # lim3 = model3.mainsequence()
    # lim4 = model4.mainsequence()
    # folder = 'MainSequence'
    # else:
    #     # full simulation
    lim1 = model1.end()
    lim2 = model2.end()
    lim3 = model3.end()
    lim4 = model4.end()
    #folder = 'FullSimulation'

    # ------ Figure ------
    fig, ax = plt.subplots(1,1)
    #ax.set_ylim(0,1)
    ax.set_xlabel('Time')
    ax.set_ylabel('Mass Fraction')
    ax.set_title(f'Central C, N & O')
    
    #if ms == True:
    # fig.suptitle(f'Main Sequence: {mass}''M$_{\odot}$', fontweight='bold')
    # limit = '_ms'
    # else:
    #     fig.suptitle(f'Full Evolution: {mass}''M$_{\odot}$', fontweight='bold')
    #     limit = ''

    # ------ Plot 1 ------
    ax.plot(model1.age[0:lim1], model1.CC[0:lim1], label = 'Carbon', color = 'navy')
    ax.plot(model1.age[0:lim1], model1.OC[0:lim1], label = 'Oxigen', color = 'darkred')
    ax.plot(model1.age[0:lim1], model1.NC[0:lim1], label = 'Nitrogen', color = 'green')
    #ax.plot(model1.age[0:lim1], model1.HeC[0:lim1], label = 'Helium', color = 'pink')
    ax.legend(shadow = False, edgecolor = 'k')
    # ax.set_xlabel('Age [Myr]')
    # ax.set_ylabel('log (H/H$_{\star}$)')
    # ax.set_title('Surface Hydrogen')
    #ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    
    plt.tight_layout()
    plt.show()
    #plt.savefig(f'Plots/{datafolder}/Subplots/Elements/{folder}/elem{mass}{limit}.png', dpi=200)

CNO(mod1,mod2,mod3,mod4)