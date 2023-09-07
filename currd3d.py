#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 23:57:35 2023

@author: benjami
"""

import netCDF4 as nc

archivo = nc.Dataset('/home/benjami/Escriptori/TFM/GETCUR/curd.nc', 'r')

variables = archivo.variables.keys()

for variable in variables:
    print(variable)



time = archivo.variables['time'][:]
lon = archivo.variables['lon'][:]
lat = archivo.variables['lat'][:]
uo = archivo.variables['uo'][:]
vo = archivo.variables['vo'][:]
dp=archivo.variables['depth'][:]


