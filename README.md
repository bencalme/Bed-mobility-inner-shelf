# Bed Mobility in the Ebro Inner-shelf

## Overview
The main objective of this work was to develop a model that would allow the extraction and processing of CMEMS data in order to determine the interaction between current bed shear-stress and wave bed shear-stress, which are responsible for sediment mobility, and study it from both a spatial and temporal perspective. This would enable the establishment of the reliability of these products for sediment dynamics calculation studies.

### Table of Contents
1. [Data Extraction and Processing](#data-extraction-and-processing)
2. [Code developer](#Code-developer)


## Data Extraction and Processing
Data processing and execution of calculus, figures and maps comprised of the execution of various Python scripts. The diagram illustrates the program's structure and the methodology employed. Initially, data downloaded include variable values at specific longitude and latitude points. The codes designed extract the values of the variables of interest for sediment sampling locations. This process was performed using linear interpolation techniques that facilitated the creation of a new grid (bcm_interpolate_waves.py & bcm_interpolate_currents.py). This data was later used to investigate the mobility of sediments in the bed. That is make through the computation of BSS resulting from the interaction between bottom currents and waves (bcm_BSS.py). The mesh generation, serves as a fundamental component in the calculation of BSS.

## Code developer
Code developer: Benjamí Calvillo from Departament d'Enginyeria Civil i Ambiental (DECA), Universitat Politècnica de Catalunya (UPC-BarcelonaTech), benjami.calvillo@upc.edu
