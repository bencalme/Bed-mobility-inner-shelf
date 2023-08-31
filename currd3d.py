#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 23:57:35 2023

@author: benjami
"""

import netCDF4 as nc

# Abre el archivo NetCDF
archivo = nc.Dataset('/home/benjami/Escriptori/TFM/GETCUR/curd.nc', 'r')

# Obtiene las variables disponibles en el archivo
variables = archivo.variables.keys()

# Imprime las variables
for variable in variables:
    print(variable)

# Cierra el archivo NetCDF


time = archivo.variables['time'][:]
lon = archivo.variables['lon'][:]
lat = archivo.variables['lat'][:]
uo = archivo.variables['uo'][:]
vo = archivo.variables['vo'][:]
dp=archivo.variables['depth'][:]


