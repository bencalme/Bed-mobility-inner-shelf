############################################
#import libreries installed on UBUNTU
############################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import scipy.io
from matplotlib.colors import LogNorm
from matplotlib.colors import Normalize
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import MultipleLocator
import matplotlib.colors as mcolors 

############################################
#Extract variables of sediment
############################################


data1 = '/home/benjami/Escriptori/TFM/MAP_COLOR/sediment.xlsx'
dat1 = pd.read_excel(data1)
lon1 = dat1['lon']
lat1 = dat1['lat']
x1 = lon1
y1 = lat1
columna1 = []
columna2 = []
with open('/home/benjami/Escriptori/TFM/bath/ldc(1).dat', 'r') as f:
    for line in f:
        line = line.strip().split()
        columna1.append(float(line[0]))
        columna2.append(float(line[1]))
xmin1, xmax1 = 0.4, 1.3
ymin1, ymax1 = 40.1, 40.9
############################################
#extract varialbes of bathimetry
############################################


dataset1 = nc.Dataset('/home/benjami/Escriptori/TFM/bath/bath.nc')
longitude1 = dataset1.variables['lon']
latitude1 = dataset1.variables['lat']
altitude1 = dataset1.variables['elevation']
lon_data1 = longitude1[:]
lat_data1 = latitude1[:]
alt_data1 = altitude1[:]
alt_data_filtered1 = np.ma.masked_where(alt_data1 >= 0, alt_data1)
datos1 = np.loadtxt('/home/benjami/Escriptori/TFM/bath/RiuEbre.dat')
columnar1_1 = datos1[:, 0]
columnar2_1 = datos1[:, 1]


############################################
#Extract variables of sediment2
############################################

data2 = '/home/benjami/Escriptori/TFM/MAP_COLOR/sediment.xlsx'
dat2 = pd.read_excel(data2)
lon2 = dat2['lon']
lat2 = dat2['lat']
x2 = lon2
y2 = lat2
columna1 = []
columna2 = []

############################################
#extract varialbes of bathimetry2
############################################
with open('/home/benjami/Escriptori/TFM/bath/ldc(1).dat', 'r') as f:
    for line in f:
        line = line.strip().split()
        columna1.append(float(line[0]))
        columna2.append(float(line[1]))
xmin2, xmax2 = 0.4, 1.3
ymin2, ymax2 = 40.1, 40.9
dataset2 = nc.Dataset('/home/benjami/Escriptori/TFM/bath/bath.nc')
longitude2 = dataset2.variables['lon']
latitude2 = dataset2.variables['lat']
altitude2 = dataset2.variables['elevation']
lon_data2 = longitude2[:]
lat_data2 = latitude2[:]
alt_data2 = altitude2[:]
alt_data_filtered2 = np.ma.masked_where(alt_data2 >= 0, alt_data2)
datos2 = np.loadtxt('/home/benjami/Escriptori/TFM/bath/RiuEbre.dat')
columnar1_2 = datos2[:, 0]
columnar2_2 = datos2[:, 1]


############################################
#Declare form of figure
############################################
fig = plt.figure(figsize=(12, 6))
gs = GridSpec(1, 2, width_ratios=[1, 1])


#define log scale
norm = mcolors.LogNorm()

############################################
#plot axes 1
############################################
ax1 = fig.add_subplot(gs[0])
scatter1 = ax1.scatter(x1, y1, c=bed_mobility_inve, cmap='jet', norm=norm)

ax1.plot(columna1, columna2, '-k')
ax1.contour(lon_data1, lat_data1, alt_data_filtered1, colors='gray', levels=100)
ax1.plot(columnar1_1, columnar2_1, '-b')
ax1.set_xlim(xmin1, xmax1)
ax1.set_ylim(ymin1, ymax1)
ax1.set_xlabel('Longitude (ºE)')
ax1.set_ylabel('Latitude (ºN)')
ax1.set_title('Bed mobility (spring-summer)')
plt.text(-0.05, 1.05, 'a)', transform=ax1.transAxes, fontsize=12, fontweight='bold')


############################################
#Plot axes Ax2
############################################

ax2 = fig.add_subplot(gs[1])
scatter2 = ax2.scatter(x2, y2, c=bed_mobility_prim, cmap='jet', norm=norm)

ax2.plot(columna1, columna2, '-k')
ax2.contour(lon_data2, lat_data2, alt_data_filtered2, colors='gray', levels=100)

ax2.plot(columnar1_2, columnar2_2, '-b')
ax2.set_xlim(xmin2, xmax2)
ax2.set_ylim(ymin2, ymax2)
ax2.set_xlabel('Longitude (ºE)')
ax2.set_ylabel('Latitude (ºN)')
ax2.set_title('Bed mobility (fall-winter)')
plt.colorbar(scatter1, ax=ax2, label='Bed mobility (%)')

plt.text(-0.05, 1.05, 'b)', transform=ax2.transAxes, fontsize=12, fontweight='bold')

plt.tight_layout()

plt.show()