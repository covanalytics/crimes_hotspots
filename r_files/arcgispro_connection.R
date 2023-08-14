
#load packages and file directories
source("r_files/package_load.R")


# Connect to the library of tools in ArcGIS Pro
## Rstudio must be 64X bit version
arcpy <- rpygeo_build_env(path = "...Python/envs/arcgispro-py3/python.exe", 
                          overwrite = TRUE,
                          extensions = "Spatial")


