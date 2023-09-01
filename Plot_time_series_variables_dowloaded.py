############################################
#import libreries installed on UBUNTU
############################################

import netCDF4 as nc
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import datetime
############################################
#Obtain and declare variables form originatl dowloaded data
############################################

data = nc.Dataset('/home/benjami/Escriptori/TFM/GETWAVES/waves.nc')
datatimex = xr.open_dataset('/home/benjami/Escriptori/TFM/GETWAVES/waves.nc')
time = datatimex.variables['time'][:]

lon = data.variables['longitude'][:]
lat = data.variables['latitude'][:]
hs = data.variables['VHM0'][:]
timedata = pd.to_datetime(time.values)


data = nc.Dataset('/home/benjami/Escriptori/TFM/GETWAVES/period.nc')

lont = data.variables['longitude'][:]
latt = data.variables['latitude'][:]
tp = data.variables['VTM01_SW1'][:]

dataxrr = xr.open_dataset('/home/benjami/Escriptori/TFM/GETCUR/curd.nc')
time_variables = dataxrr["time"]
times = pd.to_datetime(time_variables.values)


ya=[40.6]
xa=[0.8]

yb=[40.71]
xb=[0.97]

yc=[40.3]
xc=[1.2]

min_lat = np.min(lat)
max_lat = np.max(lat)

min_lon = np.min(lon)
max_lon = np.max(lon)

############################################
#Obtain point near declaration points located for mesh
############################################

latitudeshsa = np.linspace(min_lat, max_lat, num=hs.shape[1])
longitudeshsa = np.linspace(min_lon, max_lon, num=hs.shape[2])
lat_idxa = np.argmin(np.abs(latitudeshsa- ya))
lon_idxa = np.argmin(np.abs(longitudeshsa - xa))
alturaA = hs[:, lat_idxa, lon_idxa]




latitudeshsb = np.linspace(min_lat, max_lat, num=hs.shape[1])
longitudeshsb = np.linspace(min_lon, max_lon, num=hs.shape[2])
lat_idxb = np.argmin(np.abs(latitudeshsb- yb))
lon_idxb = np.argmin(np.abs(longitudeshsb - xb))
alturaB = hs[:, lat_idxb, lon_idxb]


latitudeshsc = np.linspace(min_lat, max_lat, num=hs.shape[1])
longitudeshsc = np.linspace(min_lon, max_lon, num=hs.shape[2])
lat_idxc = np.argmin(np.abs(latitudeshsc- yc))
lon_idxc = np.argmin(np.abs(longitudeshsc - xc))
alturaC = hs[:, lat_idxc, lon_idxc]





latitudestpa = np.linspace(min_lat, max_lat, num=tp.shape[1])
longitudestpsa = np.linspace(min_lon, max_lon, num=tp.shape[2])
lat_idxta = np.argmin(np.abs(latitudestpa- ya))
lon_idxta = np.argmin(np.abs(longitudestpsa - xa))
periodoA = tp[:, lat_idxta, lon_idxta]

latitudestpb = np.linspace(min_lat, max_lat, num=tp.shape[1])
longitudestpsb = np.linspace(min_lon, max_lon, num=tp.shape[2])
lat_idxtb = np.argmin(np.abs(latitudestpb- yb))
lon_idxtb = np.argmin(np.abs(longitudestpsb - xb))
periodoB = tp[:, lat_idxtb, lon_idxtb]



latitudestpc = np.linspace(min_lat, max_lat, num=tp.shape[1])
longitudestpsc = np.linspace(min_lon, max_lon, num=tp.shape[2])
lat_idxtc = np.argmin(np.abs(latitudestpc- yc))
lon_idxtc = np.argmin(np.abs(longitudestpsc - xc))
periodoC = tp[:, lat_idxtc, lon_idxtc]



min_lat = np.min(lat)
max_lat = np.max(lat)

min_lon = np.min(lon)
max_lon = np.max(lon)

velocitydata=np.sqrt((aux_uo**2)+(aux_vo**2))

latitudescura = np.linspace(min_lat, max_lat, num=velocitydata.shape[1])
longitudescursa = np.linspace(min_lon, max_lon, num=velocitydata.shape[2])

lat_idxca = np.argmin(np.abs(latitudescura- ya))
lon_idxca = np.argmin(np.abs(longitudescursa - xa))
velA = velocitydata[:, lat_idxca, lon_idxca]


latitudescurb = np.linspace(min_lat, max_lat, num=velocitydata.shape[1])
longitudescursb = np.linspace(min_lon, max_lon, num=velocitydata.shape[2])

lat_idxcb = np.argmin(np.abs(latitudescurb- yb))

lon_idxcb = np.argmin(np.abs(longitudescursb - xb))
velB = velocitydata[:, lat_idxtb, lon_idxtb]


latitudestpc = np.linspace(min_lat, max_lat, num=velocitydata.shape[1])
longitudestpsc = np.linspace(min_lon, max_lon, num=velocitydata.shape[2])

lat_idxtc = np.argmin(np.abs(latitudestpc- yc))

lon_idxtc = np.argmin(np.abs(longitudestpsc - xc))

velC = velocitydata[:, lat_idxtc, lon_idxtc]


############################################
#declare size of plot and type of plot
############################################

plt.figure(figsize=(10, 8))  
plt.subplot(3, 1, 1)  


plt.plot(timedata, alturaA, color='red',linewidth=1, label='Z1')
plt.plot(timedata, alturaB, color='orange', linewidth=0.8, label=' Z2')
plt.plot(timedata, alturaC, color='blue', linewidth=0.4, label=' Z3')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.title('Wave height (Hs)')

plt.ylabel('m')  
plt.xticks(rotation=45)
plt.text(-0.05, 1.05, 'a)', transform=plt.gca().transAxes, fontsize=12, fontweight='bold')


plt.subplot(3, 1, 2)  
plt.plot(timedata, periodoA, color='red',linewidth=1, label=' Z1')
plt.plot(timedata, periodoB,   color='orange', linewidth=0.8, label=' Z2')
plt.plot(timedata, periodoC,   color='blue', linewidth=0.4, label=' Z3')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')

plt.title('Peak period (Tp)')
plt.ylabel('s')  
plt.xticks(rotation=45)
plt.text(-0.05, 1.05, 'b)', transform=plt.gca().transAxes, fontsize=12, fontweight='bold')


plt.subplot(3, 1, 3)  
plt.plot(times, velA*100, color='red', linewidth=1, label=' Z1')
plt.plot(times, velC*60, color='orange', linewidth=0.8, label=' Z2')
plt.plot(times, velC*100, color='blue', linewidth=0.4, label=' Z3')

plt.title('Current bottom')

plt.ylabel('cm/s')  
plt.xticks(rotation=45)
plt.text(-0.05, 1.05, 'c)', transform=plt.gca().transAxes, fontsize=12, fontweight='bold')


plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()  
plt.show()  

print(np.min(velC)*100,np.min(velC)*60, np.min(velA)*100)