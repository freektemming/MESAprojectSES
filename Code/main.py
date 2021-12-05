# main.py
#
# Making plots for MESA project
#
# Freek Temming and Simon van Eeden

### Imports ###
import mesaPlot as mp
import Plotlib as pl

### Model declaration ###
LOGS_ROOT = '../LOGS'

# 12 solar mass, end of Helium burning
hist_12M_He = f'{LOGS_ROOT}/12M_He/history.data'
m_12M_He = mp.MESA()
m_12M_He.loadHistory(filename_in=hist_12M_He)

# 12 solar mass, end of main sequence
hist_12M = f'{LOGS_ROOT}/12M/history.data'
m_12M = mp.MESA()
m_12M.loadHistory(filename_in=hist_12M)

# 12 solar mass, end of main sequence Z=0.0002
hist_12M_Z0002 = f'{LOGS_ROOT}/12M_Z0.0002/history.data'
m_12M_Z0002 = mp.MESA()
m_12M_Z0002.loadHistory(filename_in=hist_12M_Z0002)

# 9 solar mass, end of main sequence
hist_9M = f'{LOGS_ROOT}/9M/history.data'
m_9M = mp.MESA()
m_9M.loadHistory(filename_in=hist_9M)

# 6 solar mass, end of main sequence
hist_6M = f'{LOGS_ROOT}/6M/history.data'
m_6M = mp.MESA()
m_6M.loadHistory(filename_in=hist_6M)

# 3 solar mass, end of main sequence
hist_3M = f'{LOGS_ROOT}/3M/history.data'
m_3M = mp.MESA()
m_3M.loadHistory(filename_in=hist_3M)

# 1 solar mass, end of main sequence
hist_1M = f'{LOGS_ROOT}/1M/history.data'
m_1M = mp.MESA()
m_1M.loadHistory(filename_in=hist_1M)

### Density vs temperature ###
pl.dens_temp(m_12M_He)

### HRD ###
pl.hrd(m_12M_He)

### HRD of all models ###
pl.hrd_multi([m_1M, m_3M, m_6M, m_9M, m_12M])

### HRD of difference metalicity ###
pl.hrd_multi([m_12M, m_12M_Z0002], custom_labels=['12M Z=0.02', '12M Z=0.0002'])

### H, He abundance ###
abun1 = ['H', 'He']
pl.abundance(m_12M_He, abun1)

### C, 0 abundance ###
abun2 = ['C', 'N', 'O']
pl.abundance(m_12M_He, abun2)

### Kippenhahn
pl.kip(m_12M_He)
