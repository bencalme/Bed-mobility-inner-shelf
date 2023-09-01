#####################
####################
#Insert this code in your terminal
#####################
####################

python -m motuclient --motu https://my.cmems-du.eu/motu-web/Motu --service-id MEDSEA_MULTIYEAR_WAV_006_012-TDS --product-id med-hcmr-wav-rean-h --longitude-min 0.4 --longitude-max 1.4 --latitude-min 4.1 --latitude-max 4.9 --date-min "2019-01-01 00:00:00" --date-max "2020-01-01 00:00:00" --variable VHM0 --variable VTM01_SW1 --variable VTM01_SW2 --out-dir <OUTPUT_DIRECTORY> --out-name <OUTPUT_FILENAME> --user <USERNAME> --pwd <PASSWORD>

