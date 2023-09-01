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

#Extract variables from data dowloaded Hs
data = nc.Dataset('/home/benjami/Escriptori/TFM/GETWAVES/waves.nc')

time = data.variables['time'][:]
lon = data.variables['longitude'][:]
lat = data.variables['latitude'][:]
hs = data.variables['VHM0'][:]

X,Y=np.meshgrid(lon,lat)
nx=len(lon)
ny=len(lat)

############################################
#Extract variables from data dowloaded sediment
############################################
datased = '/home/benjami/Escriptori/TFM/MAP_COLOR/sediment.xlsx'

dat = pd.read_excel(datased)

lonsed=dat['lon']
latsed=dat['lat']
sed=dat['media']
prof=dat['prof']
sedi = np.array(sed, dtype=np.float64)
prof = np.array(prof, dtype=np.float64)


############################################
#Interpolate data of Hs with points of latsed
############################################
hsi = np.zeros(shape=(ny, nx))
hs_rec = np.zeros(shape=(len(latsed), len(lonsed), len(time)))

msk = True
for t in range(len(time)):
    hw = data.variables['VHM0'][t, :, :]
    for i in range(nx):
        for j in range(ny):
            if msk is True:
                if hw.mask[j, i] == False:
                    hsi[j, i] = hw[j, i]
                else:
                    hsi[j, i] = np.nan
            else:
                hsi[j, i] = hw[j, i]

    hsg = scipy.interpolate.griddata((X.flatten(), Y.flatten()), hsi.flatten(), (lonsed, latsed), method='linear')
    hs_rec[:, :, t] = hsg
    

hs_rec=np.where(hs_rec >=8, 1, hs_rec)

hs_1d = np.zeros((len(time), len(lonsed)))
for g in range(len(lonsed)):
    vivi = hs_rec[g, g, :]
    hs_1d[:,g] = vivi
    
    

############################################
#IMport and declarate variable of data dowloaded Tp
############################################

data = nc.Dataset('/home/benjami/Escriptori/TFM/GETWAVES/period.nc')

timet = data.variables['time'][:]
lont = data.variables['longitude'][:]
latt = data.variables['latitude'][:]
tp = data.variables['VTM01_SW1'][:]

Xt,Yt=np.meshgrid(lont,latt)
nxt=len(lont)
nyt=len(latt)


############################################
#Interpolate data from data dowloaded Tp on sediment points
############################################

lonint, latint = np.meshgrid(lont, latt)

tp_interpol_list = []


for m in range(len(timet)):

    tp_component = tp[m, :, :]
    

    tp_component[np.isnan(tp_component)] = 0.0
    

    f = interpolate.interp2d(lonint, latint, tp_component, kind='linear')
    tp_interpol_component = f(lonsed, latsed)
    

    tp_interpol_list.append(tp_interpol_component)


tp_interpol = np.array(tp_interpol_list)
tp_interpol=np.where(tp_interpol >=16, 10, tp_interpol)
tp_interpol=np.where(tp_interpol <=1.5, 4, tp_interpol)


tp_fi= np.zeros((len(timet), len(lonsed)))
for g in range(len(lonsed)):
    vivi = tp_interpol[:, g, g]
    tp_fi[:,g] = vivi

############################################
#Calculation of wave bed shear stress with variable interpolated
############################################


tp_fi=tp_fi[:-1,:]
temp_org = tp_fi.shape[0]
numdiasper=temp_org//24
per_agrup = tp_fi[:numdiasper * 24, :].reshape(numdiasper, 24, -1)
per_final = np.mean(per_agrup, axis=1)


hs_1d=hs_1d[:-1,:]
hs_org = hs_1d.shape[0]
numdiashs=hs_org//24
hs_agrup = hs_1d[:numdiashs * 24, :].reshape(numdiashs, 24, -1)
hs_final = np.mean(hs_agrup, axis=1)

pi = math.pi
tz=per_final*0.781
urms=hs_final/tz
Uw=urms*np.sqrt(2)
A=(Uw*per_final)/(2*pi)
z0=sedi*(10**-6)/30
fwr=1.39*((A/z0)**(-0.52))
ro=1270
tensionW=0.5*ro*fwr*(Uw**2)


###############dibujar altura de olas
#num_tnes_original = tensionW.shape[0]
#numdias=num_tnes_original//24

#tens_agrup = tensionW[:numdias * 24, :].reshape(numdias, 24, -1)
#matriz_promedio_diario = np.mean(tens_agrup, axis=1)

