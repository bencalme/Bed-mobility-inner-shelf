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
#import and declarate variables of sediment samplings
############################################
datased = '/home/benjami/Escriptori/TFM/MAP_COLOR/sediment.xlsx'

dat = pd.read_excel(datased)

#variables
lonsed=dat['lon']
latsed=dat['lat']
sed=dat['media']
prof=dat['prof']

#transform variables on matix float64
sedi = np.array(sed, dtype=np.float64)
prof = np.array(prof, dtype=np.float64)

############################################
#CAlculation for critrical stress
############################################
s=2650/1270
vu=1.012*10**-6
d=(((9.81*(s-1))/(vu**2))**(1/3))*sedi
ocr=(0.24/d)+((0.055)*(1-np.exp(-0.02*d)))


###########SHIELD CALCULOS
#ow=(matriz_promedio_diario/(9.81*(2650-1270)*sedi))
#oc=(taucu/(9.81*(2650-1270)*sedi))

############################################
#CAlculation for bed shear stresss
############################################

tcvu=taucu*25
tcwv=tensionW
tcvu[:,:32]*= 1
tcwv[:,:32]*=0.01


#tm=tcvu*(1+(1.2*(tcwv/(tcwv+tcvu))**3.2))
tm=tcvu*(1+(1.2*((tcwv/(tcwv+tcvu))**3.2)))


############################################
#CAlculation of bed mobility
############################################

#extract variables for all seasons
primeros_80_dias = tm[:80]
ultimos_85_dias = tm[-85:]
tm_inve = np.vstack((primeros_80_dias, ultimos_85_dias))

############################################
#CAlculation of bed mobility spring summer
############################################

tm_prim = tm[80:-85]

bed_mobility_inve = []
bed_mobility_prim = []
bed_mobility_allyear = []



for point in range(len(latsed)):

    mobility_count = 0
    

    for day in range(165):

        if tm_inve[day][point] >= 0.05:
            mobility_count += 1
    

    mobility_percentage_inve = (mobility_count / 165) * 100
    bed_mobility_inve.append(mobility_percentage_inve)


############################################
#CAlculation of bed mobility for fall winter
############################################

for point in range(len(latsed)):

    mobility_count = 0
    

    for day in range(200):

        if tm_prim[day][point] >= 0.05:
            mobility_count += 1
    

    mobility_percentage_prim = (mobility_count / 200) * 100
    bed_mobility_prim.append(mobility_percentage_prim)

############################################
#CAlculation of bed mobility for one year
############################################


bed_mobility_allyear_list = []

for point in range(len(latsed)):

    mobility_count = 0
    

    for day in range(365):

        if tm[day][point] >= 0.05:
            mobility_count += 1
    

    bed_mobility_allyear = (mobility_count / 365) * 100
    

    bed_mobility_allyear_list.append(bed_mobility_allyear)
