from windrose import WindroseAxes
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from math import pi

#Read data dowloaded
df = pd.read_excel('C:/Users/meler/OneDrive/Escritorio/TFM/1.datos/dades_vent_ona_dir_rosa/wave.xlsx')
di = df['dire']
hs = df['hs']

# Read data dowloaded
dv = pd.read_excel('C:/Users/meler/OneDrive/Escritorio/TFM/1.datos/dades_vent_ona_dir_rosa/wind.xlsx')
dir_ = dv['dir']
v = dv['v']

# Subplots one and two
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), subplot_kw=dict(projection='windrose'))

# Third graph
ax1.bar(di, hs, normed=True, opening=0.8, edgecolor='white')
ax1.set_legend(title='Wave Height (m)')  
ax1.text(0.05, 0.95, 'a)', transform=ax1.transAxes, fontsize=12, fontweight='bold', va='top', ha='right')  

# Second graph
ax2.bar(dir_, v, normed=True, opening=0.8, edgecolor='white')
ax2.set_legend(title='Wind Velocity (m/s)')
ax2.text(0.05, 0.95, 'b)', transform=ax2.transAxes, fontsize=12, fontweight='bold', va='top', ha='right')  



#save plot on jupyter
plt.savefig('rose2004.png')

plt.show()
