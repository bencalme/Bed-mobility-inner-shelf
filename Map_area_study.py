############################################
#import libreries installed on UBUNTU
############################################

import pandas as pd
from netCDF4 import Dataset
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar

columna1 = []
columna2 = []

with open('/home/benjami/Escriptori/TFM/bath/ldc(1).dat', 'r') as f:
    for line in f:
        line = line.strip().split()
        columna1.append(float(line[0]))  
        columna2.append(float(line[1]))  


############################################
#MAke figure on of plot 1
############################################

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
xmin1, xmax1 = -10, 6
ymin1, ymax1 = 36, 44
ax1.plot(columna1, columna2, '-k')
ax1.set_xlim(xmin1, xmax1)
ax1.set_ylim(ymin1, ymax1)
ax1.set_xlabel('Longitude (º)')
ax1.set_ylabel('LAtitude (º)')
rect = Rectangle((0.4, 40.1), 1.4 - 0.4, 40.9 - 40.1, edgecolor='red', facecolor='none', linewidth=2)
ax1.add_patch(rect)
ax1.text(1.6, 40.8, "Area of study", fontsize=12, color="red")
ax1.text(-0.1, 1.08, "a)", transform=ax1.transAxes, va='top', ha='left', fontweight='bold')
ax1.text(0.8, 0.3, "MEDITERRANEAN SEA", transform=ax1.transAxes, va='center', ha='center', fontsize=12, rotation=45)


xmin2, xmax2 = 0.4, 1.4
ymin2, ymax2 = 40.1, 40.9


dataset = Dataset('/home/benjami/Escriptori/TFM/bath/bath.nc')

longitude = dataset.variables['lon']
latitude = dataset.variables['lat']
altitude = dataset.variables['elevation']

lon_data = longitude[:]
lat_data = latitude[:]
alt_data = altitude[:]

alt_data_filtered = np.ma.masked_where(alt_data >= 0, alt_data)


contour_lines = plt.contour(lon_data, lat_data, alt_data_filtered, colors='gray', levels=100)

plt.clabel(contour_lines, inline=True, fmt='%1.0f', fontsize=8, colors='gray')




datos = np.loadtxt('/home/benjami/Escriptori/TFM/bath/RiuEbre.dat')

columnar1 = datos[:, 0]
columnar2 = datos[:, 1]

plt.plot(columnar1, columnar2, '-b')

############################################
#make figure 2 on plot
############################################


ax2.text(-0.1, 1.08, "b)", transform=ax2.transAxes, va='top', ha='left', fontweight='bold')

ax2.plot(columna1, columna2, '-k')
ax2.set_xlim(xmin2, xmax2)
ax2.set_ylim(ymin2, ymax2)

data = '/home/benjami/Escriptori/TFM/MAP_COLOR/sediment.xlsx'

dat = pd.read_excel(data)

lon=dat['lon'][:]
lat=dat['lat'][:]
sed=dat['media']

x = lon
y = lat
t = sed

indices_resaltados = [5, 42, 77]


ax2.set_xlabel('Longitude (ºE)')
ax2.set_ylabel('Latitude (ºN )')
rect1 = Rectangle((0.84, 40.68), 0.99 - 0.84, 40.75 - 40.68, edgecolor='red', facecolor='none')
ax2.add_patch(rect1)
texto_rect1 = "Z1"
ax2.text(1.028, 40.715, texto_rect1, ha='center', va='center', fontsize=14, color='red', fontweight='bold')
rect2 = Rectangle((0.7, 40.55), 0.87 - 0.7, 40.67 - 40.55, edgecolor='orange', facecolor='none')
ax2.add_patch(rect2)
texto_rect2 = "Z2"
ax2.text(0.8, 40.6, texto_rect2, ha='center', va='center', fontsize=14, color='orange', fontweight='bold')
rect3 = Rectangle((1.04, 40.15), 1.25 - 1.04, 40.45 - 40.15, edgecolor='blue', facecolor='none')
ax2.add_patch(rect3)
texto = "Z3"
ax2.text(1.15, 40.3, texto, ha='center', va='center', fontsize=14, color='blue', fontweight='bold' )
handles = [rect1, rect2, rect3]
labels = ["Z1: River mouth/Inner-shelf", "Z2: Inner-shelf", "Z3: Outer-shelf"]
ax2.legend(handles, labels, loc='upper right')

plt.tight_layout()
plt.show()
