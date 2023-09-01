############################################
#import libreries installed on UBUNTU
############################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
from matplotlib.colors import LogNorm
import matplotlib.colors as mcolors

############################################
#import data of sediment sampling
############################################

data = '/home/benjami/Escriptori/TFM/MAP_COLOR/sediment.xlsx'

dat = pd.read_excel(data)

lon=dat['lon']
lat=dat['lat']

x = lon
y = lat
t = bed_mobility_allyear_list


#Log sacele
norm = mcolors.LogNorm()
plt.scatter(x, y, c=t, cmap='jet', norm=norm)
plt.colorbar(label='Bed mobility (%)')


columna1 = []
columna2 = []
############################################
#pone dat of bathimetry river
############################################

with open('/home/benjami/Escriptori/TFM/bath/ldc(1).dat', 'r') as f:
    for line in f:
        line = line.strip().split()
        columna1.append(float(line[0]))  
        columna2.append(float(line[1]))  

xmin, xmax = 0.4, 1.3
ymin, ymax = 40.1, 40.9

plt.plot(columna1, columna2, '-k')

plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

############################################
#pone dat of bathimetry 
############################################

dataset = nc.Dataset('/home/benjami/Escriptori/TFM/bath/bath.nc')

longitude = dataset.variables['lon']
latitude = dataset.variables['lat']
altitude = dataset.variables['elevation']

lon_data = longitude[:]
lat_data = latitude[:]
alt_data = altitude[:]

alt_data_filtered = np.ma.masked_where(alt_data >= 0, alt_data)


contour_lines = plt.contour(lon_data, lat_data, alt_data_filtered, colors='grey', levels=100)

plt.clabel(contour_lines, inline=True, fmt='%1.0f', fontsize=8, colors='grey')

############################################
#pone dat of bathimetry river
############################################

datos = np.loadtxt('/home/benjami/Escriptori/TFM/bath/RiuEbre.dat')

columnar1 = datos[:, 0]
columnar2 = datos[:, 1]

plt.plot(columnar1, columnar2, '-b')


plt.xlabel('Longitude (ºE)')
plt.ylabel('Latitude (ºN)')
plt.show()

############################################
#MAke boxplot anual results
############################################


# Generar datos de ejemplo bed_mobility_inve
datab1 = bed_mobility_allyear_list[0:32]
datab2 = bed_mobility_allyear_list[32:54]
datab3 = bed_mobility_allyear_list[55:79]

data_to_plot = [datab3, datab2, datab1]

box_colors = ['red', 'orange', 'blue']

fig, ax = plt.subplots()

bp = ax.boxplot(data_to_plot, patch_artist=True, boxprops=dict(facecolor='white'))

for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)

ax.set_xticklabels(['River mouth\nInner-shlef (Z1)', 'Inner-shelf  (Z2)', 'Outer-shelf (Z3)'])
ax.set_ylabel('%')

print(np.mean(datab3),np.mean(datab2),np.mean(datab1))

plt.show()