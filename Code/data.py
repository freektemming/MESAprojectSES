# script that contains data import for other scripts

from classData import Data
#from classStructure import Structure

# ------ Select Data ------
    
datafolder = '1'

# -----------------------------------------------------------------------------------

# Vink 01
mod1 = Data(f'../Data/{datafolder}/20/LOGS/out.data')
mod2 = Data(f'../Data/{datafolder}/30/LOGS/out.data')
mod3 = Data(f'../Data/{datafolder}/40/LOGS/out.data')
mod4 = Data(f'../Data/{datafolder}/50/LOGS/out.data')
mod5 = Data(f'../Data/{datafolder}/60/LOGS/out.data')
