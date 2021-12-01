# main.py
#
# Making plots for MESA project
#
# Freek Temming and Simon van Eeden

### Imports ###
from classData import Data
# import mesaPlot as mp

### Model declaration ###
LOGS_ROOT = '../LOGS'

# 12 solar mass, end of Helium burning
hist_12M_He = (f'{LOGS_ROOT}/12M_He/history.data')
# mod_12M_He= Data(hist_12M_He)
# m_12M_He = mp.MESA()
# m_12M_He.loadHistory(filename_in=hist_12M_He)

# 12 solar mass, end of main sequence
hist_12M = (f'{LOGS_ROOT}/12M/history.data')
# mod_12M= Data(hist_12M)
# m_12M = mp.MESA()
# m_12M.loadHistory(filename_in=hist_12M)

# 9 solar mass, end of main sequence
hist_9M = (f'{LOGS_ROOT}/9M/history.data')
# mod_9M= Data(hist_9M)
# m_9M = mp.MESA()
# m_9M.loadHistory(filename_in=hist_9M)

# 6 solar mass, end of main sequence
hist_6M = (f'{LOGS_ROOT}/6M/history.data')
# mod_6M= Data(hist_6M)
# m_6M = mp.MESA()
# m_6M.loadHistory(filename_in=hist_6M)

# 3 solar mass, end of main sequence
hist_3M = (f'{LOGS_ROOT}/3M/history.data')
# mod_3M= Data(hist_3M)
# m_3M = mp.MESA()
# m_3M.loadHistory(filename_in=hist_3M)

# 1 solar mass, end of main sequence
hist_1M = (f'{LOGS_ROOT}/1M/history.data')
# mod_1M= Data(hist_1M)
# m_1M = mp.MESA()
# m_1M.loadHistory(filename_in=hist_1M)

### Making plots ###
TODO

### MESAplot ###
# # Query parameter
# print(m_12M_He.hist.data['center_c12'])

# # Example plot HR diagram
# p=mp.plot()
# p.plotHR(m_12M_He)

