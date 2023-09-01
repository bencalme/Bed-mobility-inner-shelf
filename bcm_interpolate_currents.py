############################################
#import libreries installed on UBUNTU
############################################


import netCDF4 as nc
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import math

############################################
#Extrat variables from varialbes dowloaded
############################################
archivo = nc.Dataset('/home/benjami/Escriptori/TFM/GETCUR/curd.nc', 'r')

variables = archivo.variables.keys()

for variable in variables:
    print(variable)


time = archivo.variables['time'][:]
lon = archivo.variables['lon'][:]
lat = archivo.variables['lat'][:]
uo = archivo.variables['uo'][:]
vo = archivo.variables['vo'][:]
dp = archivo.variables['depth'][:]


##################
##Extract bottom variables from Uo
###################


#tDetect variables NaN
uo = np.ma.masked_values(uo, 1e+20)
vo = np.ma.masked_values(vo, 1e+20)
uo = np.ma.filled(uo, np.nan)
vo = np.ma.filled(vo, np.nan)

n_time, n_depth, n_lat, n_lon = uo.shape
aux_uo = np.full((n_time, n_lat, n_lon), np.nan, dtype=np.float64)

for t in range(n_time):
    for i in range(n_lat):
        for j in range(n_lon):

            indice = np.argmax(uo[t,:,i,j]) - 1
            uo_filled = np.ma.filled(uo[t,:,i,j], np.nan)  
            aux_uo[t,i,j] = uo_filled[indice]
            
    


##################
#extract bottom variables from Vo
###################

n_timev, n_depthv, n_latv, n_lonv = vo.shape
aux_vo = np.full((n_timev, n_latv, n_lonv), np.nan, dtype=np.float64)

for a in range(n_timev):
    for b in range(n_latv):
        for c in range(n_lonv):

            indicev = np.argmax(vo[a,:,b,c]) - 1
            vo_filled = np.ma.filled(vo[a,:,b,c], np.nan)  
            aux_vo[a,b,c] = vo_filled[indicev]



##################
#Interpolate data from Uo and Vo on sediment points
###################

###################
#Extract variables from sediment sampling##########
###################
datased = '/home/benjami/Escriptori/TFM/MAP_COLOR/sediment.xlsx'

dat = pd.read_excel(datased)

#variables
lonsed=dat['lon']
latsed=dat['lat']
sed=dat['media']
prof=dat['prof']
sedi = np.array(sed, dtype=np.float64)
prof = np.array(prof, dtype=np.float64)

###################
#Interpolation Uo
###################

lonint, latint = np.meshgrid(lon, lat)

uo_interpol_list = []


for m in range(len(time)):
    
    uo_component = aux_uo[m, :, :]
    
    
    uo_component[np.isnan(uo_component)] = 0.0
    
    # Lineal interpolation
    f = interpolate.interp2d(lonint, latint, uo_component, kind='linear')
    uo_interpol_component = f(lonsed, latsed)
    
    
    uo_interpol_list.append(uo_interpol_component)


uo_interpol = np.array(uo_interpol_list)
uo_interpol=np.where(uo_interpol >=0.5, 0.1, uo_interpol)


uo_fi= np.zeros((len(time), len(lonsed)))
for g in range(len(lonsed)):
    vivi = uo_interpol[:, g, g]
    uo_fi[:,g] = vivi


###################
#Interpolation Vo
###################

vo_interpol_list = []

for q in range(len(time)):
    vo_component = aux_vo[q, :, :]
    
    vo_component[np.isnan(vo_component)] = 0.0
    
    n = interpolate.interp2d(lonint, latint, vo_component, kind='linear')
    vo_interpol_component = n(lonsed, latsed)
    
    vo_interpol_list.append(vo_interpol_component)

vo_interpol = np.array(vo_interpol_list)
vo_interpol=np.where(vo_interpol >=0.5, 0.1, vo_interpol)

vo_fi = np.zeros((len(time), len(lonsed)))
for g in range(len(lonsed)):
    vivi = vo_interpol[:, g, g]
    vo_fi[:,g] = vivi


###################
# CAlculation of current bed shear stress
###################

vel=np.sqrt(uo_fi**2 + vo_fi**2)
dens=1270
z0=(sedi*(10**-6))/30
lo=np.log((prof*(-1))/z0)
cd=((0.4)/(lo-1))**2
tau=dens*cd*(vel**2)
taucu=tau[:-1,:]

taucu=np.where(taucu >=100, 7.6, taucu)
