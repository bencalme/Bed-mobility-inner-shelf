############################################
#import libreries installed on UBUNTU
############################################

import netCDF4 as nc
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import scipy.interpolate
import math
import datetime
from scipy.stats import ttest_rel
from scipy.stats import ttest_ind



############################################
#Extract data dowloaded by buoys and copernicus data. Declaration of varibles to compare
############################################

datacomparehs = nc.Dataset('/home/benjami/Escriptori/TFM/GETWAVES/waves.nc')
dataxr = xr.open_dataset('/home/benjami/Escriptori/TFM/GETWAVES/waves.nc')

timecom = dataxr.variables['time'][:]
loncom = datacomparehs.variables['longitude'][:]
latcom = datacomparehs.variables['latitude'][:]
hscom = datacomparehs.variables['VHM0'][:]
timecom = pd.to_datetime(timecom.values)


datacomparet = nc.Dataset('/home/benjami/Escriptori/TFM/GETWAVES/period.nc')

timetcom = datacomparet.variables['time'][:]
lontcom = datacomparet.variables['longitude'][:]
lattcom = datacomparet.variables['latitude'][:]
tpcom = datacomparet.variables['VTM01_SW1'][:]



dfcom = pd.read_excel('/home/benjami/Escriptori/TFM/compare/onatge.xlsx')
tpcompar = dfcom['tp']
hscompar = dfcom['hs']
tpcompar=tpcompar[:8761]
hscompar=hscompar[:8761]

tpcompar = np.array(tpcompar, dtype=np.float32)
hscompar = np.array(hscompar, dtype=np.float32)
latebro=40.69	
lonebro=1.47

min_lat = np.min(latcom)
max_lat = np.max(latcom)

min_lon = np.min(loncom)
max_lon = np.max(loncom)

############################################
#Obtain point for make a comparation
############################################


latitudescom = np.linspace(min_lat, max_lat, num=hscom.shape[1])
longitudescom = np.linspace(min_lon, max_lon, num=hscom.shape[2])
lat_idx = np.argmin(np.abs(latitudescom - latebro))
lon_idx = np.argmin(np.abs(longitudescom - lonebro))
altura_ola_en_punto = hscom[:, lat_idx, lon_idx]



latitudescomtp = np.linspace(min_lat, max_lat, num=tpcom.shape[1])
longitudescomtp = np.linspace(min_lon, max_lon, num=tpcom.shape[2])
lat_idxtp = np.argmin(np.abs(latitudescomtp - latebro))
lon_idxtp = np.argmin(np.abs(longitudescomtp - lonebro))
altura_ola_en_puntotp = tpcom[:, lat_idxtp, lon_idxtp]



import netCDF4 as nc
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import math
archivo = nc.Dataset('/home/benjami/Escriptori/TFM/GETCUR/curd.nc', 'r')



datacurrente = xr.open_dataset('/home/benjami/Escriptori/TFM/GETCUR/curd.nc')
time_variablecurr = datacurrente["time"]
timecurr = pd.to_datetime(time_variablecurr.values)

variables = archivo.variables.keys()

for variable in variables:
    print(variable)


time = archivo.variables['time'][:]
loncur = archivo.variables['lon'][:]
latcur = archivo.variables['lat'][:]
uo = archivo.variables['uo'][:]
vo = archivo.variables['vo'][:]
min_latc = np.min(latcur)
max_latc = np.max(latcur)

min_lonc = np.min(loncur)
max_lonc = np.max(loncur)



uocomp=uo[:,1,:,:]
vocomp=vo[:,1,:,:]
ucomparationdata=(np.sqrt((uocomp**2)+(vocomp**2)))*200


latitudescomcurr = np.linspace(min_latc, max_latc, num=ucomparationdata.shape[1])
longitudescomcurr = np.linspace(min_lonc, max_lonc, num=ucomparationdata.shape[2])
lat_idxcurr = np.argmin(np.abs(latitudescomcurr - latebro))
lon_idxcurr = np.argmin(np.abs(longitudescomcurr - lonebro))
altura_ola_en_puntocurr = ucomparationdata[:, lat_idxcurr, lon_idxcurr]



############################################
#Declare size of plot and characteristics
############################################



plt.figure(figsize=(10, 8))  
plt.subplot(2, 1, 1)  

plt.plot(timecom, tpcompar,label='Observation', color='green')
plt.plot(timecom, altura_ola_en_puntotp, label='Model (RMSD: 1.414 s & BIAS: -0.136 s )', linestyle='--', color='red', linewidth=0.6)

plt.legend() 
plt.title('Peak Period (Tp)')

plt.ylabel('s')  
plt.xticks(rotation=45)
plt.text(-0.05, 1.05, 'a)', transform=plt.gca().transAxes, fontsize=12, fontweight='bold')


plt.subplot(2, 1, 2)  
plt.plot(timecom, hscompar , label='Observation', color='green')
plt.plot(timecom, altura_ola_en_punto, label='Model (RMSD: 0.243 m & BIAS: -0.092 m)', linestyle='--', color='red', linewidth=0.6)

plt.legend()  
plt.title('Wave height (Hs)')

plt.ylabel('m') 
plt.xticks(rotation=45)
plt.text(-0.05, 1.05, 'b)', transform=plt.gca().transAxes, fontsize=12, fontweight='bold')


#plt.subplot(3, 1, 3)  
#plt.plot(timecurr, altura_ola_en_puntocurr , label='Observation', color='green')
#plt.plot(timecurr, altura_ola_en_puntocurr, label='Model (RMSD: 0.243 m & BIAS: -0.092 m)', linestyle='--', color='red', linewidth=0.6)

#plt.legend() 
#plt.title('Currents at 3 m (U)')
#plt.ylabel('cm/s') 
#plt.xticks(rotation=45)
#plt.text(-0.05, 1.05, 'c)', transform=plt.gca().transAxes, fontsize=12, fontweight='bold')



plt.tight_layout()  
plt.show()  



ntp = len(tpcompar)
#mapetp = (100/ntp) * np.sum(np.abs(((tpcompar) - (altura_ola_en_puntotp)) / (tpcompar)))
rmsdtp = np.sqrt(np.sum((np.array(tpcompar) - np.array(altura_ola_en_puntotp))**2) / ntp)
biastp = np.sum((altura_ola_en_puntotp) - (tpcompar)) / ntp
rmsdhtp = np.sqrt((((tpcompar) - (altura_ola_en_puntotp))**2))
rmsdhtp_mean=np.mean(rmsdhtp)
t_statistictt, p_valuett = ttest_rel(rmsdhtp, [rmsdhtp_mean] * len(rmsdhtp))

t_statistict, p_valuet = ttest_ind(tpcompar, altura_ola_en_puntotp)

############################################
#calculus for errors data
############################################

nhs = len(hscompar)
#mapehs = (100/nhs) * np.sum(np.abs(((hscompar) - (altura_ola_en_punto)) / (hscompar)))
rmsdhs = np.sqrt(np.sum(((hscompar) - (altura_ola_en_punto))**2) / nhs)
biashs = np.sum((altura_ola_en_punto) - (hscompar)) / nhs
rmsdhss = np.sqrt((((hscompar) - (altura_ola_en_punto))**2))
rmsdhss_mean=np.mean(rmsdhss)
t_statistichh, p_valuehh = ttest_rel(rmsdhss, [rmsdhss_mean] * len(rmsdhss))
t_statistih, p_valueh = ttest_ind(hscompar, altura_ola_en_punto)


############################################
#obtain mean values of errors p valuers
############################################



print("Mean Absolute Percentage Error (MAPE):", mapehs, rmsdtp, biastp,p_valuet, p_valuett)
print("Mean Absolute Percentage Error (MAPE):", mapetp, rmsdhs, biashs,p_valueh, p_valuehh)

#print("Mean Absolute Percentage Error (MAPE):", rmsdcur, biascur,p_valuec)



