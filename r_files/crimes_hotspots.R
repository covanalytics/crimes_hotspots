
source("R Files/package_load.R")


#reticulate::py_install('rpytools')
# Connect to the library of tools in ArcGIS Pro
## Rstudio must be 64X bit version
arcpy <- rpygeo_build_env(path = "C:/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe", 
                          overwrite = TRUE,
                          extensions = "Spatial")


#reticulate::source_python("hot_spot_script.py")


#system('python U:/Projects/Police/hot_spot_script.py')

