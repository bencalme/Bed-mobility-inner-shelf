############################################
#import libreries installed on UBUNTU
############################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import scipy.io
from matplotlib.colors import LogNorm
from matplotlib.colors import Normalize
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Circle, FancyArrowPatch
import matplotlib.colors as mcolors
from matplotlib.patches import Ellipse
import pandas as pd

############################################
#Obtain varialbes of bathymetry
############################################


columna1 = []
columna2 = []
with open('/home/benjami/Escriptori/TFM/bath/ldc(1).dat', 'r') as f:
    for line in f:
        line = line.strip().split()
        columna1.append(float(line[0]))
        columna2.append(float(line[1]))
xmin1, xmax1 = 0.4, 1.3
ymin1, ymax1 = 40.1, 40.9


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
#Obtain variables of bathymetry
############################################


columna1 = []
columna2 = []

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
#Make figure and characteristics patch
############################################


fig = plt.figure(figsize=(12, 6))
gs = GridSpec(1, 2, width_ratios=[1, 1])




ax1 = fig.add_subplot(gs[0])
ax1.plot(columna1, columna2, '-k')
ax1.contour(lon_data1, lat_data1, alt_data_filtered1, colors='gray', levels=100)
ax1.plot(columnar1_1, columnar2_1, '-b')
ax1.set_xlim(xmin1, xmax1)
ax1.set_ylim(ymin1, ymax1)
ax1.set_xlabel('Longitude (ºE)')
ax1.set_ylabel('Latitude (ºN)')
#ax1.set_title('Bed mobility (fall-winter)')
plt.text(-0.05, 1.05, 'a)', transform=ax1.transAxes, fontsize=12, fontweight='bold')

ellipse = Ellipse((0.86, 40.6), width=0.2, height=0.4, angle=135, fill=True, color='red', alpha=1)
plt.gca().add_patch(ellipse)


plt.text(0.85, 40.6, 'Wave stress domain', color='black', fontsize=12, ha='center', va='center', fontweight='bold', rotation=45)

ellipse = Ellipse((1.15, 40.3), width=0.2, height=0.4, angle=135, fill=True, color='blue', alpha=1)
plt.gca().add_patch(ellipse)


plt.text(1.15, 40.3, 'Current stress domain', color='black', fontsize=12, ha='center', va='center', fontweight='bold', rotation=45)



ax2 = fig.add_subplot(gs[1])

ax2.plot(columna1, columna2, '-k')
ax2.contour(lon_data2, lat_data2, alt_data_filtered2, colors='gray', levels=100)
ax2.plot(columnar1_2, columnar2_2, '-b')
ax2.set_xlim(xmin2, xmax2)
ax2.set_ylim(ymin2, ymax2)
ax2.set_xlabel('Longitude (ºE)')
ax2.set_ylabel('Latitude (ºN)')
plt.text(-0.05, 1.05, 'b)', transform=ax2.transAxes, fontsize=12, fontweight='bold')

circle2 = Circle((0.95, 40.715), radius=0.06, fill=True, color='orange', alpha=1)
ax2.add_patch(circle2)
plt.text(1.05, 40.715, 'High bed mobility', color='black', fontsize=12, ha='center', va='center', fontweight='bold', rotation=0)
ellipse2 = Ellipse((0.79, 40.58), width=0.09, height=0.3, angle=130, fill=True, color='lightgreen', alpha=1)
ax2.add_patch(ellipse2)
plt.text(0.79, 40.58, 'Medium bed mobility', color='black', fontsize=12, ha='center', va='center', fontweight='bold', rotation=45)
ellipse2 = Ellipse((1.15, 40.3), width=0.2, height=0.4, angle=135, fill=True, color='pink', alpha=1)
ax2.add_patch(ellipse2)
plt.text(1.15, 40.3, 'Low bed mobility', color='black', fontsize=12, ha='center', va='center', fontweight='bold', rotation=45)




plt.tight_layout()


plt.show()
