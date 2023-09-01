############################################
#import libreries installed on UBUNTU
############################################


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import xarray as xr
import scipy.io
import netCDF4 as nc
from netCDF4 import Dataset

############################################
#Extract variables of sediment
############################################

data = '/home/benjami/Escriptori/TFM/MAP_COLOR/sediment.xlsx'

dat = pd.read_excel(data)

lon=dat['lon']
lat=dat['lat']
sed=dat['media']

columna1 = []
columna2 = []

with open('/home/benjami/Escriptori/TFM/bath/ldc(1).dat', 'r') as f:
    for line in f:
        line = line.strip().split()
        columna1.append(float(line[0]))  
        columna2.append(float(line[1]))  

dataset = Dataset('/home/benjami/Escriptori/TFM/bath/bath.nc')
longitude = dataset.variables['lon']
latitude = dataset.variables['lat']
altitude = dataset.variables['elevation']

lon_data = longitude[:]
lat_data = latitude[:]
alt_data = altitude[:]
alt_data_filtered = np.ma.masked_where(alt_data >= 0, alt_data)

datos = np.loadtxt('/home/benjami/Escriptori/TFM/bath/RiuEbre.dat')
columnar1 = datos[:, 0]
columnar2 = datos[:, 1]

xmin, xmax = 0.72, 0.9
ymin, ymax = 40.5, 40.7


############################################
#Declare figure what i want to print an his characteristics
############################################

fig = plt.figure(figsize=(10, 14))
gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1], height_ratios=[1, 1])

ax1 = fig.add_subplot(gs[0, 0])
scatter1 = ax1.scatter(lon, lat, c=sed, cmap='jet')
ax1.plot(columna1, columna2, '-k')
ax1.contour(lon_data, lat_data, alt_data_filtered, colors='gray', levels=100)

ax1.set_xlim(xmin, xmax)
ax1.set_ylim(ymin, ymax)
ax1.set_xlabel('Longitude (ºE)')
ax1.set_ylabel('Latitude (ºN)')
ax1.set_title('Z1: River mouth/Inner-shlef')
plt.text(-0.1, 1.05, 'a)', transform=ax1.transAxes, fontsize=12, fontweight='bold')

ax2 = fig.add_subplot(gs[0, 1])
scatter2 = ax2.scatter(lon, lat, c=sed, cmap='jet')
ax2.plot(columna1, columna2, '-k')
ax2.contour(lon_data, lat_data, alt_data_filtered, colors='gray', levels=100)
ax2.plot(columnar1, columnar2, '-b')

xmin1, xmax1 = 0.88, 0.96
ymin1, ymax1 = 40.65, 40.77
ax2.set_xlim(xmin1, xmax1)
ax2.set_ylim(ymin1, ymax1)

ax2.set_xlabel('Longitude (ºE)')
ax2.set_ylabel('Latitude (ºN)')
ax2.set_title('Z2: Inner-shlef')
plt.text(-0.1, 1.05, 'b)', transform=ax2.transAxes, fontsize=12, fontweight='bold')

ax3 = fig.add_subplot(gs[1, :])
scatter3 = ax3.scatter(lon, lat, c=sed, cmap='jet')
ax3.plot(columna1, columna2, '-k')


ax3.contour(lon_data, lat_data, alt_data_filtered, colors='gray', levels=100)

ax3.plot(columnar1, columnar2, '-b')


ax3.set_xlim(xmin, xmax)
ax3.set_ylim(ymin, ymax)
ax3.set_xlabel('Longitude (ºE)')
ax3.set_ylabel('Latitude (ºN)')
xmin2, xmax2 = 0.4, 1.3
ymin2, ymax2 = 40.1, 40.9
ax3.set_xlim(xmin2, xmax2)
ax3.set_ylim(ymin2, ymax2)

plt.colorbar(scatter3, ax=ax3, label='d50 [μm]')
plt.text(-0.05, 1.05, 'c)', transform=ax3.transAxes, fontsize=12, fontweight='bold')

plt.tight_layout()

plt.show()
