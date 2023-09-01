#####################
####################
#Insert this code in your terminal
#####################
####################

python -m motuclient --motu https://my.cmems-du.eu/motu-web/Motu --service-id MEDSEA_MULTIYEAR_PHY_006_004-TDS --product-id med-cmcc-cur-rean-d --longitude-min 0.4 --longitude-max 1.4 --latitude-min 4.1 --latitude-max 4.9 --date-min "2019-01-01 00:00:00" --date-max "2020-01-01 00:00:00" --depth-min 1.0182366371154785 --depth-max 318.133544921875 --variable uo --variable vo --out-dir <OUTPUT_DIRECTORY> --out-name <OUTPUT_FILENAME> --user <USERNAME> --pwd <PASSWORD>