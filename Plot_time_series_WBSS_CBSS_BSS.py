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
import netCDF4 as nc
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import math

############################################
#Extract variables from currents to make a time plot series
############################################
archivo = nc.Dataset('/home/benjami/Escriptori/TFM/GETCUR/curd.nc', 'r')
datacurrente = xr.open_dataset('/home/benjami/Escriptori/TFM/GETCUR/curd.nc')
time_variablecurr = datacurrente["time"]

############################################
#Convert data from correct representation values
############################################
timecurr = pd.to_datetime(time_variablecurr.values)

variables = archivo.variables.keys()
for variable in variables:
    print(variable)


time = archivo.variables['time'][:]

############################################
#MAke plot for 3 figures on one plot
############################################

plt.figure(figsize=(10, 8))  
plt.subplot(3, 1, 1)  

plt.plot(timecurr[:-1], tcwv[:,60],label='Z1: River Mouth/Inner-shelf', color='red')

plt.plot(timecurr[:-1], (tcwv[:,40]*1.2),label='Z2: Inner-shlef', color='orange')
plt.plot(timecurr[:-1], tcwv[:,15], label='Z3: Outer-shlef', color='blue')

plt.legend()  
plt.title('Wave bed shear-stress')

plt.ylabel('Pa')  
plt.xticks(rotation=45)
plt.text(-0.05, 1.05, 'a)', transform=plt.gca().transAxes, fontsize=12, fontweight='bold')


plt.subplot(3, 1, 2)  
plt.plot(timecurr[:-1], tcvu[:,60],label='Z1: River Mouth/Inner-shelf', color='red')

plt.plot(timecurr[:-1], tcvu[:,40]*1.4,label='Z2: Inner-shlef', color='orange')
plt.plot(timecurr[:-1], tcvu[:,15], label='Z3: Outer-shlef', color='blue')

plt.title('Current bed shear-stress')
#plt.xlabel('Tiempo')  
plt.ylabel('Pa')  
plt.xticks(rotation=45)
plt.text(-0.05, 1.05, 'b)', transform=plt.gca().transAxes, fontsize=12, fontweight='bold')

plt.subplot(3, 1, 3)  
plt.plot(timecurr[:-1], tm[:,60],label='Z1: River Mouth/Inner-shelf', color='red')

plt.plot(timecurr[:-1], tm[:,50],label='Z2: Inner-shlef', color='orange')
plt.plot(timecurr[:-1], tm[:,15] , label='Z3: Outer-shlef', color='blue')

plt.title('Bed shear-stress')

plt.ylabel('Pa')  
plt.xticks(rotation=45)

plt.text(-0.05, 1.05, 'c)', transform=plt.gca().transAxes, fontsize=12, fontweight='bold')


plt.tight_layout()  
plt.show()  

############################################
#Declare mean shear stresss for one location to obtaing the average results
############################################

taucu1 = tcvu[:,30]
taucu2 = tcvu[:,40]
taucu3 = tcvu[:,60]

tw1 = tcwv[:,30]
tw2 = tcwv[:,40]
tw3 = tcwv[:,60]

tm1 = tm[:,30]*0.7
tm2 = tm[:,40]
tm3 = tm[:,60]


############################################
#Determine de mean results of sehar stress
############################################
mediataucu=np.mean(taucu1)
mediatw=np.mean(tw1)
metidatmfinal=np.mean(tm1)

mediataucu1=np.mean(taucu2)
mediatw1=np.mean(tw2)
metidatmfinal1=np.mean(tm2)

mediataucu2=np.mean(taucu3)
mediatw2=np.mean(tw3)
metidatmfinal2=np.mean(tm3)

