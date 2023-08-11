



import arcpy
from datetime import date
import datetime


arcpy.env.workspace = ".../Projects/Weekly_Crime_Hotspot"

today = datetime.date.today()
today_name = today.strftime('%b_%d_%Y')
##Burglaries
burgs_update = map_dir + "/burglaries_daily.shp"
burgs_update_output = "burglaries_daily" + "_" + today_name
##Auto-Thefts
theft_update = map_dir + "/vehicle_thefts_daily.shp"
theft_update_output = "vehicle_thefts_daily" + "_" + today_name
##Robberies
robbery_update = map_dir + "/robberies_daily.shp"
robbery_update_output = "robberies_daily" + "_" + today_name
##Theft from Motor Vehicl
v_theft_update = map_dir + "/thefts_from_vehicle_daily.shp"
v_theft_update_output = "thefts_from_vehicle_daily" + "_" + today_name
##Vehicle Mischief
v_mischief_update = map_dir + "/vehicle_mischief_daily.shp"
v_mischief_update_output = "vehicle_mischief_daily" + "_" + today_name
####################################
######## Add Shapefile Layers ######
####################################
#Add Burglary Layer with date in name
burglaries = arcpy.management.MakeFeatureLayer(burgs_update, 
                                  burgs_update_output, 
                                  '', 
                                  None, 
                                  "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;IncdntN IncdntN VISIBLE NONE;Priorty Priorty VISIBLE NONE;IncdntT IncdntT VISIBLE NONE;Address Address VISIBLE NONE;UntNmbr UntNmbr VISIBLE NONE;Date Date VISIBLE NONE;ArrvlTm ArrvlTm VISIBLE NONE;ClosdTm ClosdTm VISIBLE NONE;DsptcT1 DsptcT1 VISIBLE NONE;ArrvlT1 ArrvlT1 VISIBLE NONE;ClsdTm1 ClsdTm1 VISIBLE NONE;RspnsTM RspnsTM VISIBLE NONE;OnScnTM OnScnTM VISIBLE NONE;TtlClTM TtlClTM VISIBLE NONE;Year Year VISIBLE NONE;Categry Categry VISIBLE NONE;GnRprtd GnRprtd VISIBLE NONE;NbhdLbl NbhdLbl VISIBLE NONE;ID_1 ID_1 HIDDEN NONE;Beat Beat VISIBLE NONE;PIDN PIDN VISIBLE NONE;UntsOnS UntsOnS VISIBLE NONE;UntsDsp UntsDsp HIDDEN NONE;UntsCnc UntsCnc HIDDEN NONE;CnclldC CnclldC HIDDEN NONE;Count Count VISIBLE NONE")

#Add Vehicle Theft Layer with date in name
vehicle_thefts = arcpy.management.MakeFeatureLayer(theft_update, 
                                  theft_update_output, 
                                  '', 
                                  None, 
                                  "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;IncdntN IncdntN VISIBLE NONE;Priorty Priorty VISIBLE NONE;IncdntT IncdntT VISIBLE NONE;Address Address VISIBLE NONE;UntNmbr UntNmbr VISIBLE NONE;Date Date VISIBLE NONE;ArrvlTm ArrvlTm VISIBLE NONE;ClosdTm ClosdTm VISIBLE NONE;DsptcT1 DsptcT1 VISIBLE NONE;ArrvlT1 ArrvlT1 VISIBLE NONE;ClsdTm1 ClsdTm1 VISIBLE NONE;RspnsTM RspnsTM VISIBLE NONE;OnScnTM OnScnTM VISIBLE NONE;TtlClTM TtlClTM VISIBLE NONE;Year Year VISIBLE NONE;Categry Categry VISIBLE NONE;GnRprtd GnRprtd VISIBLE NONE;NbhdLbl NbhdLbl VISIBLE NONE;ID_1 ID_1 HIDDEN NONE;Beat Beat VISIBLE NONE;PIDN PIDN VISIBLE NONE;UntsOnS UntsOnS VISIBLE NONE;UntsDsp UntsDsp HIDDEN NONE;UntsCnc UntsCnc HIDDEN NONE;CnclldC CnclldC HIDDEN NONE;Count Count VISIBLE NONE")

#Add Robbery Layer with date in name
robberies = arcpy.management.MakeFeatureLayer(robbery_update, 
                                  robbery_update_output, 
                                  '', 
                                  None, 
                                  "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;IncdntN IncdntN VISIBLE NONE;Priorty Priorty VISIBLE NONE;IncdntT IncdntT VISIBLE NONE;Address Address VISIBLE NONE;UntNmbr UntNmbr VISIBLE NONE;Date Date VISIBLE NONE;ArrvlTm ArrvlTm VISIBLE NONE;ClosdTm ClosdTm VISIBLE NONE;DsptcT1 DsptcT1 VISIBLE NONE;ArrvlT1 ArrvlT1 VISIBLE NONE;ClsdTm1 ClsdTm1 VISIBLE NONE;RspnsTM RspnsTM VISIBLE NONE;OnScnTM OnScnTM VISIBLE NONE;TtlClTM TtlClTM VISIBLE NONE;Year Year VISIBLE NONE;Categry Categry VISIBLE NONE;GnRprtd GnRprtd VISIBLE NONE;NbhdLbl NbhdLbl VISIBLE NONE;ID_1 ID_1 HIDDEN NONE;Beat Beat VISIBLE NONE;PIDN PIDN VISIBLE NONE;UntsOnS UntsOnS VISIBLE NONE;UntsDsp UntsDsp HIDDEN NONE;UntsCnc UntsCnc HIDDEN NONE;CnclldC CnclldC HIDDEN NONE;Count Count VISIBLE NONE")

#Add Thefts from Vehicle Layer with date in name
thefts_from_vehicle = arcpy.management.MakeFeatureLayer(v_theft_update, 
                                  v_theft_update_output, 
                                  '', 
                                  None, 
                                  "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;IncdntN IncdntN VISIBLE NONE;Priorty Priorty VISIBLE NONE;IncdntT IncdntT VISIBLE NONE;Address Address VISIBLE NONE;UntNmbr UntNmbr VISIBLE NONE;Date Date VISIBLE NONE;ArrvlTm ArrvlTm VISIBLE NONE;ClosdTm ClosdTm VISIBLE NONE;DsptcT1 DsptcT1 VISIBLE NONE;ArrvlT1 ArrvlT1 VISIBLE NONE;ClsdTm1 ClsdTm1 VISIBLE NONE;RspnsTM RspnsTM VISIBLE NONE;OnScnTM OnScnTM VISIBLE NONE;TtlClTM TtlClTM VISIBLE NONE;Year Year VISIBLE NONE;Categry Categry VISIBLE NONE;GnRprtd GnRprtd VISIBLE NONE;NbhdLbl NbhdLbl VISIBLE NONE;ID_1 ID_1 HIDDEN NONE;Beat Beat VISIBLE NONE;PIDN PIDN VISIBLE NONE;UntsOnS UntsOnS VISIBLE NONE;UntsDsp UntsDsp HIDDEN NONE;UntsCnc UntsCnc HIDDEN NONE;CnclldC CnclldC HIDDEN NONE;Count Count VISIBLE NONE")

#Add Criminal Vehicle Mischief  with date in name
vehicle_mischief = arcpy.management.MakeFeatureLayer(v_mischief_update, 
                                  v_mischief_update_output, 
                                  '', 
                                  None, 
                                  "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;IncdntN IncdntN VISIBLE NONE;Priorty Priorty VISIBLE NONE;IncdntT IncdntT VISIBLE NONE;Address Address VISIBLE NONE;UntNmbr UntNmbr VISIBLE NONE;Date Date VISIBLE NONE;ArrvlTm ArrvlTm VISIBLE NONE;ClosdTm ClosdTm VISIBLE NONE;DsptcT1 DsptcT1 VISIBLE NONE;ArrvlT1 ArrvlT1 VISIBLE NONE;ClsdTm1 ClsdTm1 VISIBLE NONE;RspnsTM RspnsTM VISIBLE NONE;OnScnTM OnScnTM VISIBLE NONE;TtlClTM TtlClTM VISIBLE NONE;Year Year VISIBLE NONE;Categry Categry VISIBLE NONE;GnRprtd GnRprtd VISIBLE NONE;NbhdLbl NbhdLbl VISIBLE NONE;ID_1 ID_1 HIDDEN NONE;Beat Beat VISIBLE NONE;PIDN PIDN VISIBLE NONE;UntsOnS UntsOnS VISIBLE NONE;UntsDsp UntsDsp HIDDEN NONE;UntsCnc UntsCnc HIDDEN NONE;CnclldC CnclldC HIDDEN NONE;Count Count VISIBLE NONE")


####################################
######## Project Shapefile Layers ##
####################################
#Project Burglaries Layer
burgs_prj = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/burgs_daily_prj" + "_" + today_name
arcpy.management.Project(burgs_update_output,
                         burgs_prj, 
                         'PROJCS["NAD_1983_2011_StatePlane_Kentucky_North_FIPS_1601_Ft_US",GEOGCS["GCS_NAD_1983_2011",DATUM["D_NAD_1983_2011",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",1640416.666666667],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-84.25],PARAMETER["Standard_Parallel_1",37.96666666666667],PARAMETER["Standard_Parallel_2",38.96666666666667],PARAMETER["Latitude_Of_Origin",37.5],UNIT["Foot_US",0.3048006096012192]]', "WGS_1984_(ITRF08)_To_NAD_1983_2011", 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', 
                         "NO_PRESERVE_SHAPE", 
                         None, 
                         "NO_VERTICAL")
#Project Vehicle Thefts Layer
theft_prj = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/theft_daily_prj" + "_" + today_name
arcpy.management.Project(theft_update_output,
                         theft_prj, 
                         'PROJCS["NAD_1983_2011_StatePlane_Kentucky_North_FIPS_1601_Ft_US",GEOGCS["GCS_NAD_1983_2011",DATUM["D_NAD_1983_2011",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",1640416.666666667],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-84.25],PARAMETER["Standard_Parallel_1",37.96666666666667],PARAMETER["Standard_Parallel_2",38.96666666666667],PARAMETER["Latitude_Of_Origin",37.5],UNIT["Foot_US",0.3048006096012192]]', "WGS_1984_(ITRF08)_To_NAD_1983_2011", 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', 
                         "NO_PRESERVE_SHAPE", 
                         None, 
                         "NO_VERTICAL")
#Project Robbery Layer
robbery_prj = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/robbery_daily_prj" + "_" + today_name
arcpy.management.Project(robbery_update_output,
                         robbery_prj, 
                         'PROJCS["NAD_1983_2011_StatePlane_Kentucky_North_FIPS_1601_Ft_US",GEOGCS["GCS_NAD_1983_2011",DATUM["D_NAD_1983_2011",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",1640416.666666667],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-84.25],PARAMETER["Standard_Parallel_1",37.96666666666667],PARAMETER["Standard_Parallel_2",38.96666666666667],PARAMETER["Latitude_Of_Origin",37.5],UNIT["Foot_US",0.3048006096012192]]', "WGS_1984_(ITRF08)_To_NAD_1983_2011", 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', 
                         "NO_PRESERVE_SHAPE", 
                         None, 
                         "NO_VERTICAL")
#Project Thefts from Vehicle Layer
vehicle_theft_prj = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/theft_from_vehicle_daily_prj" + "_" + today_name
arcpy.management.Project(v_theft_update_output,
                         vehicle_theft_prj, 
                         'PROJCS["NAD_1983_2011_StatePlane_Kentucky_North_FIPS_1601_Ft_US",GEOGCS["GCS_NAD_1983_2011",DATUM["D_NAD_1983_2011",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",1640416.666666667],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-84.25],PARAMETER["Standard_Parallel_1",37.96666666666667],PARAMETER["Standard_Parallel_2",38.96666666666667],PARAMETER["Latitude_Of_Origin",37.5],UNIT["Foot_US",0.3048006096012192]]', "WGS_1984_(ITRF08)_To_NAD_1983_2011", 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', 
                         "NO_PRESERVE_SHAPE", 
                         None, 
                         "NO_VERTICAL")
#Project Criminal Vehicle mischief 
vehicle_mischief_prj = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/vehicle_mischief_daily_prj" + "_" + today_name
arcpy.management.Project(v_mischief_update_output,
                         vehicle_mischief_prj, 
                         'PROJCS["NAD_1983_2011_StatePlane_Kentucky_North_FIPS_1601_Ft_US",GEOGCS["GCS_NAD_1983_2011",DATUM["D_NAD_1983_2011",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",1640416.666666667],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-84.25],PARAMETER["Standard_Parallel_1",37.96666666666667],PARAMETER["Standard_Parallel_2",38.96666666666667],PARAMETER["Latitude_Of_Origin",37.5],UNIT["Foot_US",0.3048006096012192]]', "WGS_1984_(ITRF08)_To_NAD_1983_2011", 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', 
                         "NO_PRESERVE_SHAPE", 
                         None, 
                         "NO_VERTICAL")                         
                         
######################
###Space-time cubes###
######################
#create space-time cube for 1 week, 300 ft (burglaries, auto-thefts, robberies)
burgs_cube = arcpy.env.workspace + "/burgs_cube_weekly.nc"
arcpy.stpm.CreateSpaceTimeCube(burgs_prj, burgs_cube,"Date",None, "1 Weeks", "END_TIME", None, "300 Feet", "Count SUM ZEROS", "HEXAGON_GRID", None, None)

theft_cube = arcpy.env.workspace + "/vtheft_cube_weekly.nc"
arcpy.stpm.CreateSpaceTimeCube(theft_prj,         #projected shapefile
                               theft_cube,        #data cube
                               "Date",            #Time field
                               None,              #Template cube
                               "1 Weeks",         #Time step interval
                               "END_TIME",        #Time step alignment; how aggregation occurs
                               None, 
                               "1800 Feet",        #Size of bins to aggregate points
                               "Count SUM ZEROS", #Summary fields
                               "HEXAGON_GRID",    #The shape of the polygon mesh to aggregate points
                               None, None)
robbery_cube = arcpy.env.workspace + "/robbery_cube_weekly.nc"
arcpy.stpm.CreateSpaceTimeCube(robbery_prj, 
                               robbery_cube,
                               "Date",
                               None, 
                               "1 Weeks", 
                               "END_TIME", 
                               None, 
                               "1800 Feet", 
                               "Count SUM ZEROS", 
                               "HEXAGON_GRID", None, None)
vehicle_theft_cube = arcpy.env.workspace + "/vehicle_theft_cube_weekly.nc"
arcpy.stpm.CreateSpaceTimeCube(vehicle_theft_prj, 
                               vehicle_theft_cube,
                               "Date",
                               None, 
                               "1 Weeks", 
                               "END_TIME", 
                               None, 
                               "1800 Feet", 
                               "Count SUM ZEROS", 
                               "HEXAGON_GRID", None, None)
vehicle_mischief_cube = arcpy.env.workspace + "/vehicle_mischief_cube_weekly.nc"
arcpy.stpm.CreateSpaceTimeCube(vehicle_mischief_prj, 
                               vehicle_mischief_cube,
                               "Date",
                               None, 
                               "1 Weeks", 
                               "END_TIME", 
                               None, 
                               "1800 Feet", 
                               "Count SUM ZEROS", 
                               "HEXAGON_GRID", None, None)                               

#########################################################
######  Emerging Hot Spot Analysis for Crimes #######    
######################################################### 
#Emerging hot spot analysis (300 ft; 1 week is aggregated as time intervals )
burg_spot_path = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Burg_Analysis_Emerging_HotSpot"
with arcpy.EnvManager(scratchWorkspace = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb", 
                      workspace = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb"):
                      arcpy.stpm.EmergingHotSpotAnalysis(burgs_cube, 
                      "COUNT_SUM_ZEROS", 
                       burg_spot_path, 
                       "1800 Feet", 
                       2, None, "FIXED_DISTANCE", 6, "ENTIRE_CUBE")
arcpy.management.CalculateField(burg_spot_path, "TYPE", '"Burglary"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")

theft_spot_path = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/VTheft_Analysis_Emerging_HotSpot"
with arcpy.EnvManager(scratchWorkspace = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb", 
                      workspace = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb"):
                      arcpy.stpm.EmergingHotSpotAnalysis(theft_cube, 
                      "COUNT_SUM_ZEROS", 
                       theft_spot_path, 
                       "1800 Feet", 
                       2, None, "FIXED_DISTANCE", 6, "ENTIRE_CUBE")
arcpy.management.CalculateField(theft_spot_path, "TYPE", '"Theft-Motor Vehicle"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")        
        
robbery_spot_path = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Robbery_Analysis_Emerging_HotSpot"
with arcpy.EnvManager(scratchWorkspace = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb", 
                      workspace = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb"):
                      arcpy.stpm.EmergingHotSpotAnalysis(robbery_cube, 
                      "COUNT_SUM_ZEROS", 
                       robbery_spot_path, 
                       "1800 Feet", 
                       2, None, "FIXED_DISTANCE", 6, "ENTIRE_CUBE")       
arcpy.management.CalculateField(robbery_spot_path, "TYPE", '"Robbery"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")    

vehicle_theft_spot_path = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Vehicle_Theft_Analysis_Emerging_HotSpot"
with arcpy.EnvManager(scratchWorkspace = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb", 
                      workspace = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb"):
                      arcpy.stpm.EmergingHotSpotAnalysis(vehicle_theft_cube, 
                      "COUNT_SUM_ZEROS", 
                       vehicle_theft_spot_path, 
                       "1800 Feet", 
                       2, None, "FIXED_DISTANCE", 6, "ENTIRE_CUBE")       
arcpy.management.CalculateField(vehicle_theft_spot_path, "TYPE", '"Theft-From a Motor Vehicle"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS") 
  
vehicle_mischief_spot_path = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Vehicle_Mischief_Analysis_Emerging_HotSpot"
with arcpy.EnvManager(scratchWorkspace = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb", 
                      workspace = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb"):
                      arcpy.stpm.EmergingHotSpotAnalysis(vehicle_mischief_cube, 
                      "COUNT_SUM_ZEROS", 
                       vehicle_mischief_spot_path, 
                       "1800 Feet", 
                       2, None, "FIXED_DISTANCE", 6, "ENTIRE_CUBE")       
arcpy.management.CalculateField(vehicle_mischief_spot_path, "TYPE", '"Criminal Mischief-Auto"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS") 
                
#Apply symbology template to emerging hot spot analysis layer
#emrg_export = arcpy.management.ApplySymbologyFromLayer(ht_spot_path, 
                                         #arcpy.env.workspace + "/Emerging_Hot_Spot_Symbology.lyrx", 
                                         #"VALUE_FIELD PATTERN PATTERN", "DEFAULT")
        

###########################################
######  Optimized Hot Spot Analysis #######    
########################################### 
#create minimum bounding box based on projected points 
burg_box = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/burg_box"
arcpy.management.MinimumBoundingGeometry(burgs_prj, 
                                         burg_box, 
                                         "CONVEX_HULL", "ALL", None, "NO_MBG_FIELDS") 
theft_box = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/theft_box"
arcpy.management.MinimumBoundingGeometry(theft_prj, 
                                         theft_box, 
                                         "CONVEX_HULL", "ALL", None, "NO_MBG_FIELDS") 
robbery_box = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/robbery_box"
arcpy.management.MinimumBoundingGeometry(robbery_prj, 
                                         robbery_box, 
                                         "CONVEX_HULL", "ALL", None, "NO_MBG_FIELDS")
vehicle_theft_box = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/vehicle_theft_box"
arcpy.management.MinimumBoundingGeometry(vehicle_theft_prj, 
                                         vehicle_theft_box, 
                                         "CONVEX_HULL", "ALL", None, "NO_MBG_FIELDS")
                                        
vehicle_mischief_box = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/vehicle_mischief_box"
arcpy.management.MinimumBoundingGeometry(vehicle_mischief_prj, 
                                         vehicle_mischief_box, 
                                         "CONVEX_HULL", "ALL", None, "NO_MBG_FIELDS")  
                                         
#Optimized Hot Spot Masked to Minimum Bounding of Project Points 
burg_hot_spot = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Burg_OptimizedHotSpotAnalysis"
arcpy.stats.OptimizedHotSpotAnalysis(burgs_prj, 
                                     burg_hot_spot, 
                                     None, 
                                     "COUNT_INCIDENTS_WITHIN_HEXAGON_POLYGONS", 
                                     burg_box, None, None, "300 Feet", "600 Feet")
arcpy.management.CalculateField(burg_hot_spot, "TYPE", '"Burglary"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")

theft_hot_spot = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Theft_OptimizedHotSpotAnalysis"
arcpy.stats.OptimizedHotSpotAnalysis(theft_prj, 
                                     theft_hot_spot, 
                                     None, 
                                     "COUNT_INCIDENTS_WITHIN_HEXAGON_POLYGONS", 
                                     theft_box, None, None, "300 Feet", "600 Feet")
arcpy.management.CalculateField(theft_hot_spot, "TYPE", '"Theft-Motor Vehicle"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")

robbery_hot_spot = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Robbery_OptimizedHotSpotAnalysis"
arcpy.stats.OptimizedHotSpotAnalysis(robbery_prj, 
                                     robbery_hot_spot, 
                                     None, 
                                     "COUNT_INCIDENTS_WITHIN_HEXAGON_POLYGONS", 
                                     robbery_box, None, None, "300 Feet", "600 Feet")
arcpy.management.CalculateField(robbery_hot_spot, "TYPE", '"Robbery"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")

vehicle_theft_hot_spot = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Vehicle_Theft_OptimizedHotSpotAnalysis"
arcpy.stats.OptimizedHotSpotAnalysis(vehicle_theft_prj, 
                                     vehicle_theft_hot_spot, 
                                     None, 
                                     "COUNT_INCIDENTS_WITHIN_HEXAGON_POLYGONS", 
                                     vehicle_theft_box, None, None, "300 Feet", "600 Feet")
arcpy.management.CalculateField(vehicle_theft_hot_spot, "TYPE", '"Theft-From a Motor Vehicle"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")

vehicle_mischief_hot_spot = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Vehicle_Mischief_OptimizedHotSpotAnalysis"
arcpy.stats.OptimizedHotSpotAnalysis(vehicle_mischief_prj, 
                                     vehicle_mischief_hot_spot, 
                                     None, 
                                     "COUNT_INCIDENTS_WITHIN_HEXAGON_POLYGONS", 
                                     vehicle_mischief_box, None, None, "300 Feet", "600 Feet")
arcpy.management.CalculateField(vehicle_mischief_hot_spot, "TYPE", '"Criminal Mischief-Auto"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")

#####################################################
## Create Copies of Layer Output for ArcGIS online###
#####################################################
#Emerging Hot Spot Output
arcpy.management.CopyFeatures(burg_spot_path, 
                             arcpy.env.workspace + "/Burglary_Emerging_Final.shp", 
                              '', None, None, None)  
arcpy.management.CopyFeatures(theft_spot_path, 
                             arcpy.env.workspace + "/VTheft_Emerging_Final.shp", 
                              '', None, None, None) 
arcpy.management.CopyFeatures(robbery_spot_path, 
                             arcpy.env.workspace + "/Robbery_Emerging_Final.shp", 
                              '', None, None, None) 
arcpy.management.CopyFeatures(vehicle_theft_spot_path, 
                             arcpy.env.workspace + "/Theft_From_Vehicle_Emerging_Final.shp", 
                              '', None, None, None) 
arcpy.management.CopyFeatures(vehicle_mischief_spot_path, 
                             arcpy.env.workspace + "/Vehicle_Mischief_Emerging_Final.shp", 
                              '', None, None, None) 
#Points Output
arcpy.management.CopyFeatures(burglaries, 
                              arcpy.env.workspace + "/Burglaries.shp", 
                              '', None, None, None)

arcpy.management.CopyFeatures(vehicle_thefts, 
                              arcpy.env.workspace + "/Vehicle_Thefts.shp", 
                              '', None, None, None)

arcpy.management.CopyFeatures(robberies, 
                              arcpy.env.workspace + "/Robberies.shp", 
                              '', None, None, None)

arcpy.management.CopyFeatures(thefts_from_vehicle, 
                              arcpy.env.workspace + "/Thefts_from_Vehicle.shp", 
                              '', None, None, None)
arcpy.management.CopyFeatures(vehicle_mischief, 
                              arcpy.env.workspace + "/Vehicle_Mischief.shp", 
                              '', None, None, None)                              
#Optimal Hot Spot Output
arcpy.management.CopyFeatures(burg_hot_spot, 
                              arcpy.env.workspace + "/Burglary_Optimal_Hot_spot.shp", 
                              '', None, None, None)
arcpy.management.CopyFeatures(theft_hot_spot, 
                              arcpy.env.workspace + "/VTheft_Optimal_Hot_spot.shp", 
                              '', None, None, None)
arcpy.management.CopyFeatures(robbery_hot_spot, 
                              arcpy.env.workspace + "/Robbery_Optimal_Hot_spot.shp", 
                              '', None, None, None)
arcpy.management.CopyFeatures(vehicle_theft_hot_spot, 
                              arcpy.env.workspace + "/Thefts_from_Vehicle_Optimal_Hot_spot.shp", 
                              '', None, None, None)
arcpy.management.CopyFeatures(vehicle_mischief_hot_spot, 
                              arcpy.env.workspace + "/Vehicle_Mischief_Optimal_Hot_spot.shp", 
                              '', None, None, None)
################################
### Merge Final Layers #########
################################

#Emerging Hot Spots
Burglary_Emerging_Final = arcpy.env.workspace + "/Burglary_Emerging_Final.shp"
VTheft_Emerging_Final = arcpy.env.workspace + "/VTheft_Emerging_Final.shp"
Robbery_Emerging_Final = arcpy.env.workspace + "/Robbery_Emerging_Final.shp"
Theft_From_Vehicle_Emerging_Final = arcpy.env.workspace + "/Theft_From_Vehicle_Emerging_Final.shp"
Vehicle_Mischief_Emerging_Final = arcpy.env.workspace + "/Vehicle_Mischief_Emerging_Final.shp"


emerging_list = [Burglary_Emerging_Final, VTheft_Emerging_Final, Robbery_Emerging_Final, Theft_From_Vehicle_Emerging_Final, Vehicle_Mischief_Emerging_Final]



arcpy.management.Merge(emerging_list,
                      arcpy.env.workspace + "/Emerging_Hot_Spots_FinalA.shp",  
                       'LOCATION "LOCATION" true true false 10 Long 0 10,First,#,Burglary_Emerging_Final,LOCATION,-1,-1,VTheft_Emerging_Final,LOCATION,-1,-1,Robbery_Emerging_Final,LOCATION,-1,-1,Theft_From_Vehicle_Emerging_Final,LOCATION,-1,-1,Vehicle_Mischief_Emerging_Final,LOCATION,-1,-1;CATEGORY "CATEGORY" true true false 10 Long 0 10,First,#,Burglary_Emerging_Final,CATEGORY,-1,-1,VTheft_Emerging_Final,CATEGORY,-1,-1,Robbery_Emerging_Final,CATEGORY,-1,-1,Theft_From_Vehicle_Emerging_Final,CATEGORY,-1,-1,Vehicle_Mischief_Emerging_Final,CATEGORY,-1,-1;PATTERN "PATTERN" true true false 254 Text 0 0,First,#,Burglary_Emerging_Final,PATTERN,0,254,VTheft_Emerging_Final,PATTERN,0,254,Robbery_Emerging_Final,PATTERN,0,254,Theft_From_Vehicle_Emerging_Final,PATTERN,0,254,Vehicle_Mischief_Emerging_Final,PATTERN,0,254;PERC_HOT "PERC_HOT" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,PERC_HOT,-1,-1,VTheft_Emerging_Final,PERC_HOT,-1,-1,Robbery_Emerging_Final,PERC_HOT,-1,-1,Theft_From_Vehicle_Emerging_Final,PERC_HOT,-1,-1,Vehicle_Mischief_Emerging_Final,PERC_HOT,-1,-1;PERC_COLD "PERC_COLD" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,PERC_COLD,-1,-1,VTheft_Emerging_Final,PERC_COLD,-1,-1,Robbery_Emerging_Final,PERC_COLD,-1,-1,Theft_From_Vehicle_Emerging_Final,PERC_COLD,-1,-1,Vehicle_Mischief_Emerging_Final,PERC_COLD,-1,-1;TREND_Z "TREND_Z" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,TREND_Z,-1,-1,VTheft_Emerging_Final,TREND_Z,-1,-1,Robbery_Emerging_Final,TREND_Z,-1,-1,Theft_From_Vehicle_Emerging_Final,TREND_Z,-1,-1,Vehicle_Mischief_Emerging_Final,TREND_Z,-1,-1;TREND_P "TREND_P" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,TREND_P,-1,-1,VTheft_Emerging_Final,TREND_P,-1,-1,Robbery_Emerging_Final,TREND_P,-1,-1,Theft_From_Vehicle_Emerging_Final,TREND_P,-1,-1,Vehicle_Mischief_Emerging_Final,TREND_P,-1,-1;TREND_BIN "TREND_BIN" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,TREND_BIN,-1,-1,VTheft_Emerging_Final,TREND_BIN,-1,-1,Robbery_Emerging_Final,TREND_BIN,-1,-1,Theft_From_Vehicle_Emerging_Final,TREND_BIN,-1,-1,Vehicle_Mischief_Emerging_Final,TREND_BIN,-1,-1;SUM_VALUE "SUM_VALUE" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,SUM_VALUE,-1,-1,VTheft_Emerging_Final,SUM_VALUE,-1,-1,Robbery_Emerging_Final,SUM_VALUE,-1,-1,Theft_From_Vehicle_Emerging_Final,SUM_VALUE,-1,-1,Vehicle_Mischief_Emerging_Final,SUM_VALUE,-1,-1;MIN_VALUE "MIN_VALUE" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,MIN_VALUE,-1,-1,VTheft_Emerging_Final,MIN_VALUE,-1,-1,Robbery_Emerging_Final,MIN_VALUE,-1,-1,Theft_From_Vehicle_Emerging_Final,MIN_VALUE,-1,-1,Vehicle_Mischief_Emerging_Final,MIN_VALUE,-1,-1;MAX_VALUE "MAX_VALUE" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,MAX_VALUE,-1,-1,VTheft_Emerging_Final,MAX_VALUE,-1,-1,Robbery_Emerging_Final,MAX_VALUE,-1,-1,Theft_From_Vehicle_Emerging_Final,MAX_VALUE,-1,-1,Vehicle_Mischief_Emerging_Final,MAX_VALUE,-1,-1;MEAN_VALUE "MEAN_VALUE" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,MEAN_VALUE,-1,-1,VTheft_Emerging_Final,MEAN_VALUE,-1,-1,Robbery_Emerging_Final,MEAN_VALUE,-1,-1,Theft_From_Vehicle_Emerging_Final,MEAN_VALUE,-1,-1,Vehicle_Mischief_Emerging_Final,MEAN_VALUE,-1,-1;STD_VALUE "STD_VALUE" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,STD_VALUE,-1,-1,VTheft_Emerging_Final,STD_VALUE,-1,-1,Robbery_Emerging_Final,STD_VALUE,-1,-1,Theft_From_Vehicle_Emerging_Final,STD_VALUE,-1,-1,Vehicle_Mischief_Emerging_Final,STD_VALUE,-1,-1;MED_VALUE "MED_VALUE" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,MED_VALUE,-1,-1,VTheft_Emerging_Final,MED_VALUE,-1,-1,Robbery_Emerging_Final,MED_VALUE,-1,-1,Theft_From_Vehicle_Emerging_Final,MED_VALUE,-1,-1,Vehicle_Mischief_Emerging_Final,MED_VALUE,-1,-1;Shape_Leng "Shape_Leng" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,Shape_Leng,-1,-1,VTheft_Emerging_Final,Shape_Leng,-1,-1,Robbery_Emerging_Final,Shape_Leng,-1,-1,Theft_From_Vehicle_Emerging_Final,Shape_Leng,-1,-1,Vehicle_Mischief_Emerging_Final,Shape_Leng,-1,-1;Shape_Area "Shape_Area" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,Shape_Area,-1,-1,VTheft_Emerging_Final,Shape_Area,-1,-1,Robbery_Emerging_Final,Shape_Area,-1,-1,Theft_From_Vehicle_Emerging_Final,Shape_Area,-1,-1,Vehicle_Mischief_Emerging_Final,Shape_Area,-1,-1;TYPE "TYPE" true true false 254 Text 0 0,First,#,Burglary_Emerging_Final,TYPE,0,254,VTheft_Emerging_Final,TYPE,0,254,Robbery_Emerging_Final,TYPE,0,254,Theft_From_Vehicle_Emerging_Final,TYPE,0,254,Vehicle_Mischief_Emerging_Final,TYPE,0,254', "NO_SOURCE_INFO")



#arcpy.management.Merge(emerging_list,
#                      arcpy.env.workspace + "/Emerging_Hot_Spots_FinalA.shp", 
#                       'LOCATION "LOCATION" true true false 10 Long 0 10,First,#,Burglary_Emerging_Final,LOCATION,-1,-1,VTheft_Emerging_Final,LOCATION,-1,-1,Robbery_Emerging_Final,LOCATION,-1,-1,Theft_From_Vehicle_Emerging_Final,LOCATION,-1,-1;CATEGORY "CATEGORY" true true false 10 Long 0 10,First,#,Burglary_Emerging_Final,CATEGORY,-1,-1,VTheft_Emerging_Final,CATEGORY,-1,-1,Robbery_Emerging_Final,CATEGORY,-1,-1,Theft_From_Vehicle_Emerging_Final,CATEGORY,-1,-1;PATTERN "PATTERN" true true false 254 Text 0 0,First,#,Burglary_Emerging_Final,PATTERN,0,254,VTheft_Emerging_Final,PATTERN,0,254,Robbery_Emerging_Final,PATTERN,0,254,Theft_From_Vehicle_Emerging_Final,PATTERN,0,254;PERC_HOT "PERC_HOT" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,PERC_HOT,-1,-1,VTheft_Emerging_Final,PERC_HOT,-1,-1,Robbery_Emerging_Final,PERC_HOT,-1,-1,Theft_From_Vehicle_Emerging_Final,PERC_HOT,-1,-1;PERC_COLD "PERC_COLD" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,PERC_COLD,-1,-1,VTheft_Emerging_Final,PERC_COLD,-1,-1,Robbery_Emerging_Final,PERC_COLD,-1,-1,Theft_From_Vehicle_Emerging_Final,PERC_COLD,-1,-1;TREND_Z "TREND_Z" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,TREND_Z,-1,-1,VTheft_Emerging_Final,TREND_Z,-1,-1,Robbery_Emerging_Final,TREND_Z,-1,-1,Theft_From_Vehicle_Emerging_Final,TREND_Z,-1,-1;TREND_P "TREND_P" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,TREND_P,-1,-1,VTheft_Emerging_Final,TREND_P,-1,-1,Robbery_Emerging_Final,TREND_P,-1,-1,Theft_From_Vehicle_Emerging_Final,TREND_P,-1,-1;TREND_BIN "TREND_BIN" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,TREND_BIN,-1,-1,VTheft_Emerging_Final,TREND_BIN,-1,-1,Robbery_Emerging_Final,TREND_BIN,-1,-1,Theft_From_Vehicle_Emerging_Final,TREND_BIN,-1,-1;SUM_VALUE "SUM_VALUE" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,SUM_VALUE,-1,-1,VTheft_Emerging_Final,SUM_VALUE,-1,-1,Robbery_Emerging_Final,SUM_VALUE,-1,-1,Theft_From_Vehicle_Emerging_Final,SUM_VALUE,-1,-1;MIN_VALUE "MIN_VALUE" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,MIN_VALUE,-1,-1,VTheft_Emerging_Final,MIN_VALUE,-1,-1,Robbery_Emerging_Final,MIN_VALUE,-1,-1,Theft_From_Vehicle_Emerging_Final,MIN_VALUE,-1,-1;MAX_VALUE "MAX_VALUE" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,MAX_VALUE,-1,-1,VTheft_Emerging_Final,MAX_VALUE,-1,-1,Robbery_Emerging_Final,MAX_VALUE,-1,-1,Theft_From_Vehicle_Emerging_Final,MAX_VALUE,-1,-1;MEAN_VALUE "MEAN_VALUE" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,MEAN_VALUE,-1,-1,VTheft_Emerging_Final,MEAN_VALUE,-1,-1,Robbery_Emerging_Final,MEAN_VALUE,-1,-1,Theft_From_Vehicle_Emerging_Final,MEAN_VALUE,-1,-1;STD_VALUE "STD_VALUE" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,STD_VALUE,-1,-1,VTheft_Emerging_Final,STD_VALUE,-1,-1,Robbery_Emerging_Final,STD_VALUE,-1,-1,Theft_From_Vehicle_Emerging_Final,STD_VALUE,-1,-1;MED_VALUE "MED_VALUE" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,MED_VALUE,-1,-1,VTheft_Emerging_Final,MED_VALUE,-1,-1,Robbery_Emerging_Final,MED_VALUE,-1,-1,Theft_From_Vehicle_Emerging_Final,MED_VALUE,-1,-1;Shape_Leng "Shape_Leng" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,Shape_Leng,-1,-1,VTheft_Emerging_Final,Shape_Leng,-1,-1,Robbery_Emerging_Final,Shape_Leng,-1,-1,Theft_From_Vehicle_Emerging_Final,Shape_Leng,-1,-1;Shape_Area "Shape_Area" true true false 19 Double 0 0,First,#,Burglary_Emerging_Final,Shape_Area,-1,-1,VTheft_Emerging_Final,Shape_Area,-1,-1,Robbery_Emerging_Final,Shape_Area,-1,-1,Theft_From_Vehicle_Emerging_Final,Shape_Area,-1,-1;TYPE "TYPE" true true false 254 Text 0 0,First,#,Burglary_Emerging_Final,TYPE,0,254,VTheft_Emerging_Final,TYPE,0,254,Robbery_Emerging_Final,TYPE,0,254,Theft_From_Vehicle_Emerging_Final,TYPE,0,254', "NO_SOURCE_INFO")



arcpy.analysis.Select(arcpy.env.workspace + "/Emerging_Hot_Spots_FinalA.shp", 
                      arcpy.env.workspace + "/Emerging_Hot_Spots_Final.shp", 
                      "PATTERN NOT IN ('No Pattern Detected')")

#Optimal Hot Spots
Burglary_Optimal_Hot_spot = arcpy.env.workspace + "/Burglary_Optimal_Hot_spot.shp"
VTheft_Optimal_Hot_spot = arcpy.env.workspace + "/VTheft_Optimal_Hot_spot.shp"
Robbery_Optimal_Hot_spot = arcpy.env.workspace + "/Robbery_Optimal_Hot_spot.shp"
Thefts_from_Vehicle_Optimal_Hot_spot = arcpy.env.workspace + "/Thefts_from_Vehicle_Optimal_Hot_spot.shp"
Vehicle_Mischief_Optimal_Hot_spot = arcpy.env.workspace + "/Vehicle_Mischief_Optimal_Hot_spot.shp"


optimal_list = [Burglary_Optimal_Hot_spot, VTheft_Optimal_Hot_spot, Robbery_Optimal_Hot_spot, Thefts_from_Vehicle_Optimal_Hot_spot, Vehicle_Mischief_Optimal_Hot_spot]

arcpy.management.Merge(optimal_list, 
                       arcpy.env.workspace + "/Optimal_Hot_SpotsA.shp", 
                       'SOURCE_ID "SOURCE_ID" true true false 10 Long 0 10,First,#,Burglary_Optimal_Hot_spot,SOURCE_ID,-1,-1,VTheft_Optimal_Hot_spot,SOURCE_ID,-1,-1,Robbery_Optimal_Hot_spot,SOURCE_ID,-1,-1,Thefts_from_Vehicle_Optimal_Hot_spot,SOURCE_ID,-1,-1,Vehicle_Mischief_Optimal_Hot_spot,SOURCE_ID,-1,-1;JOIN_COUNT "JOIN_COUNT" true true false 10 Long 0 10,First,#,Burglary_Optimal_Hot_spot,JOIN_COUNT,-1,-1,VTheft_Optimal_Hot_spot,JOIN_COUNT,-1,-1,Robbery_Optimal_Hot_spot,JOIN_COUNT,-1,-1,Thefts_from_Vehicle_Optimal_Hot_spot,JOIN_COUNT,-1,-1,Vehicle_Mischief_Optimal_Hot_spot,JOIN_COUNT,-1,-1;Shape_Leng "Shape_Leng" true true false 19 Double 0 0,First,#,Burglary_Optimal_Hot_spot,Shape_Leng,-1,-1,VTheft_Optimal_Hot_spot,Shape_Leng,-1,-1,Robbery_Optimal_Hot_spot,Shape_Leng,-1,-1,Thefts_from_Vehicle_Optimal_Hot_spot,Shape_Leng,-1,-1,Vehicle_Mischief_Optimal_Hot_spot,Shape_Leng,-1,-1;Shape_Area "Shape_Area" true true false 19 Double 0 0,First,#,Burglary_Optimal_Hot_spot,Shape_Area,-1,-1,VTheft_Optimal_Hot_spot,Shape_Area,-1,-1,Robbery_Optimal_Hot_spot,Shape_Area,-1,-1,Thefts_from_Vehicle_Optimal_Hot_spot,Shape_Area,-1,-1,Vehicle_Mischief_Optimal_Hot_spot,Shape_Area,-1,-1;GiZScore "GiZScore" true true false 19 Double 0 0,First,#,Burglary_Optimal_Hot_spot,GiZScore,-1,-1,VTheft_Optimal_Hot_spot,GiZScore,-1,-1,Robbery_Optimal_Hot_spot,GiZScore,-1,-1,Thefts_from_Vehicle_Optimal_Hot_spot,GiZScore,-1,-1,Vehicle_Mischief_Optimal_Hot_spot,GiZScore,-1,-1;GiPValue "GiPValue" true true false 19 Double 0 0,First,#,Burglary_Optimal_Hot_spot,GiPValue,-1,-1,VTheft_Optimal_Hot_spot,GiPValue,-1,-1,Robbery_Optimal_Hot_spot,GiPValue,-1,-1,Thefts_from_Vehicle_Optimal_Hot_spot,GiPValue,-1,-1,Vehicle_Mischief_Optimal_Hot_spot,GiPValue,-1,-1;NNeighbors "NNeighbors" true true false 10 Long 0 10,First,#,Burglary_Optimal_Hot_spot,NNeighbors,-1,-1,VTheft_Optimal_Hot_spot,NNeighbors,-1,-1,Robbery_Optimal_Hot_spot,NNeighbors,-1,-1,Thefts_from_Vehicle_Optimal_Hot_spot,NNeighbors,-1,-1,Vehicle_Mischief_Optimal_Hot_spot,NNeighbors,-1,-1;Gi_Bin "Gi_Bin" true true false 10 Long 0 10,First,#,Burglary_Optimal_Hot_spot,Gi_Bin,-1,-1,VTheft_Optimal_Hot_spot,Gi_Bin,-1,-1,Robbery_Optimal_Hot_spot,Gi_Bin,-1,-1,Thefts_from_Vehicle_Optimal_Hot_spot,Gi_Bin,-1,-1,Vehicle_Mischief_Optimal_Hot_spot,Gi_Bin,-1,-1;TYPE "TYPE" true true false 254 Text 0 0,First,#,Burglary_Optimal_Hot_spot,TYPE,0,254,VTheft_Optimal_Hot_spot,TYPE,0,254,Robbery_Optimal_Hot_spot,TYPE,0,254,Thefts_from_Vehicle_Optimal_Hot_spot,TYPE,0,254,Vehicle_Mischief_Optimal_Hot_spot,TYPE,0,254', "NO_SOURCE_INFO")


arcpy.analysis.Select(arcpy.env.workspace + "/Optimal_Hot_SpotsA.shp", 
                      arcpy.env.workspace + "/Optimal_Hot_Spots_Final.shp", 
                      "Gi_Bin = 3")

#Crimes
Robberies = arcpy.env.workspace + "/Robberies.shp"
Vehicle_Thefts = arcpy.env.workspace + "/Vehicle_Thefts.shp"
Burglaries = arcpy.env.workspace + "/Burglaries.shp"
Thefts_from_Vehicle = arcpy.env.workspace + "/Thefts_from_Vehicle.shp"
Vehicle_Mischief = arcpy.env.workspace + "/Vehicle_Mischief.shp"


crime_list = [Robberies, Vehicle_Thefts, Burglaries, Thefts_from_Vehicle, Vehicle_Mischief]

arcpy.management.Merge(crime_list, 
                       arcpy.env.workspace + "/Crimes.shp", 
                       'IncdntN "IncdntN" true true false 80 Text 0 0,First,#,Robberies,IncdntN,0,80,Vehicle_Thefts,IncdntN,0,80,Burglaries,IncdntN,0,80,Thefts_from_Vehicle,IncdntN,0,80,Vehicle_Mischief,IncdntN,0,80;Priorty "Priorty" true true false 80 Text 0 0,First,#,Robberies,Priorty,0,80,Vehicle_Thefts,Priorty,0,80,Burglaries,Priorty,0,80,Thefts_from_Vehicle,Priorty,0,80,Vehicle_Mischief,Priorty,0,80;IncdntT "IncdntT" true true false 80 Text 0 0,First,#,Robberies,IncdntT,0,80,Vehicle_Thefts,IncdntT,0,80,Burglaries,IncdntT,0,80,Thefts_from_Vehicle,IncdntT,0,80,Vehicle_Mischief,IncdntT,0,80;Address "Address" true true false 80 Text 0 0,First,#,Robberies,Address,0,80,Vehicle_Thefts,Address,0,80,Burglaries,Address,0,80,Thefts_from_Vehicle,Address,0,80,Vehicle_Mischief,Address,0,80;UntNmbr "UntNmbr" true true false 80 Text 0 0,First,#,Robberies,UntNmbr,0,80,Vehicle_Thefts,UntNmbr,0,80,Burglaries,UntNmbr,0,80,Thefts_from_Vehicle,UntNmbr,0,80,Vehicle_Mischief,UntNmbr,0,80;Date "Date" true true false 8 Date 0 0,First,#,Robberies,Date,-1,-1,Vehicle_Thefts,Date,-1,-1,Burglaries,Date,-1,-1,Thefts_from_Vehicle,Date,-1,-1,Vehicle_Mischief,Date,-1,-1;ArrvlTm "ArrvlTm" true true false 80 Text 0 0,First,#,Robberies,ArrvlTm,0,80,Vehicle_Thefts,ArrvlTm,0,80,Burglaries,ArrvlTm,0,80,Thefts_from_Vehicle,ArrvlTm,0,80,Vehicle_Mischief,ArrvlTm,0,80;Date2 "Date2" true true false 8 Date 0 0,First,#,Robberies,Date2,-1,-1,Vehicle_Thefts,Date2,-1,-1,Burglaries,Date2,-1,-1,Thefts_from_Vehicle,Date2,-1,-1,Vehicle_Mischief,Date2,-1,-1;Count "Count" true true false 19 Double 15 18,First,#,Robberies,Count,-1,-1,Vehicle_Thefts,Count,-1,-1,Burglaries,Count,-1,-1,Thefts_from_Vehicle,Count,-1,-1,Vehicle_Mischief,Count,-1,-1;AREA "AREA" true true false 19 Double 15 18,First,#,Robberies,AREA,-1,-1,Vehicle_Thefts,AREA,-1,-1,Burglaries,AREA,-1,-1,Thefts_from_Vehicle,AREA,-1,-1,Vehicle_Mischief,AREA,-1,-1;PERIMET "PERIMET" true true false 19 Double 15 18,First,#,Robberies,PERIMET,-1,-1,Vehicle_Thefts,PERIMET,-1,-1,Burglaries,PERIMET,-1,-1,Thefts_from_Vehicle,PERIMET,-1,-1,Vehicle_Mischief,PERIMET,-1,-1;CITYBND_ "CITYBND_" true true false 9 Long 0 9,First,#,Robberies,CITYBND_,-1,-1,Vehicle_Thefts,CITYBND_,-1,-1,Burglaries,CITYBND_,-1,-1,Thefts_from_Vehicle,CITYBND_,-1,-1,Vehicle_Mischief,CITYBND_,-1,-1;CITYBND_I "CITYBND_I" true true false 9 Long 0 9,First,#,Robberies,CITYBND_I,-1,-1,Vehicle_Thefts,CITYBND_I,-1,-1,Burglaries,CITYBND_I,-1,-1,Thefts_from_Vehicle,CITYBND_I,-1,-1,Vehicle_Mischief,CITYBND_I,-1,-1;CITY "CITY" true true false 80 Text 0 0,First,#,Robberies,CITY,0,80,Vehicle_Thefts,CITY,0,80,Burglaries,CITY,0,80,Thefts_from_Vehicle,CITY,0,80,Vehicle_Mischief,CITY,0,80;CITY_ "CITY_" true true false 80 Text 0 0,First,#,Robberies,CITY_,0,80,Vehicle_Thefts,CITY_,0,80,Burglaries,CITY_,0,80,Thefts_from_Vehicle,CITY_,0,80,Vehicle_Mischief,CITY_,0,80;SYMBOL "SYMBOL" true true false 9 Long 0 9,First,#,Robberies,SYMBOL,-1,-1,Vehicle_Thefts,SYMBOL,-1,-1,Burglaries,SYMBOL,-1,-1,Thefts_from_Vehicle,SYMBOL,-1,-1,Vehicle_Mischief,SYMBOL,-1,-1;ACREAGE "ACREAGE" true true false 19 Double 15 18,First,#,Robberies,ACREAGE,-1,-1,Vehicle_Thefts,ACREAGE,-1,-1,Burglaries,ACREAGE,-1,-1,Thefts_from_Vehicle,ACREAGE,-1,-1,Vehicle_Mischief,ACREAGE,-1,-1;Shp_Lng "Shp_Lng" true true false 19 Double 15 18,First,#,Robberies,Shp_Lng,-1,-1,Vehicle_Thefts,Shp_Lng,-1,-1,Burglaries,Shp_Lng,-1,-1,Thefts_from_Vehicle,Shp_Lng,-1,-1;Shap_Ar "Shap_Ar" true true false 19 Double 15 18,First,#,Robberies,Shap_Ar,-1,-1,Vehicle_Thefts,Shap_Ar,-1,-1,Burglaries,Shap_Ar,-1,-1,Thefts_from_Vehicle,Shap_Ar,-1,-1,Vehicle_Mischief,Shap_Ar,-1,-1;Citylbl "Citylbl" true true false 80 Text 0 0,First,#,Robberies,Citylbl,0,80,Vehicle_Thefts,Citylbl,0,80,Burglaries,Citylbl,0,80,Thefts_from_Vehicle,Citylbl,0,80,Vehicle_Mischief,Citylbl,0,80;SqMiles "SqMiles" true true false 19 Double 15 18,First,#,Robberies,SqMiles,-1,-1,Vehicle_Thefts,SqMiles,-1,-1,Burglaries,SqMiles,-1,-1,Thefts_from_Vehicle,SqMiles,-1,-1,Vehicle_Mischief,SqMiles,-1,-1;Shap_Lng "Shap_Lng" true true false 19 Double 15 18,First,#,Vehicle_Mischief,Shap_Lng,-1,-1;Shp_Lngt "Shp_Lngt" true true false 19 Double 15 18,First,#,Vehicle_Mischief,Shp_Lngt,-1,-1', "NO_SOURCE_INFO")

with arcpy.EnvManager(scratchWorkspace=arcpy.env.workspace + "/Crimes.shp", 
                      workspace=arcpy.env.workspace + "/Crimes.shp"):
    arcpy.ca.AddDateAttributes("Crimes", "Date", "DAY_FULL_NAME Date_DW;HOUR Date_HR;MONTH Date_MO;DAY_OF_MONTH Date_DM;YEAR Date_YR")
 
crimes = arcpy.env.workspace + "/Crimes.shp" 
    
arcpy.management.CalculateField(crimes, "Date_1", "Date($feature.Date2)", "ARCADE", '', "DATE", "ENFORCE_DOMAINS")   

arcpy.management.CalculateField(crimes, "Date_1", 'DateAdd($feature.Date_1,1,"days")', "ARCADE", '', "DATE", "ENFORCE_DOMAINS")

arcpy.management.CalculateField(crimes, "Date_1Text", "Text($feature.Date_1, 'M/D/Y')", "ARCADE", '', "TEXT", "ENFORCE_DOMAINS")


#Kernel Density of all crimes
out_raster = arcpy.sa.KernelDensity(crimes, "NONE", 0.000190484264833231, None, "SQUARE_MAP_UNITS", "DENSITIES", "PLANAR", None);
out_raster.save(arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Kernel_Density")


# Reclassifying kernel density raster
kernel_density = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Kernel_Density"

arcpy.ddd.Reclassify(kernel_density, "VALUE", "0 72522.317647 1;72522.317647 247784.585294 2;247784.585294 489525.644118 3;489525.644118 870267.811765 4;870267.811765 1541099.250000 5", 
arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Kernel_Density_Reclass", "DATA")


#creating contour polygon of reclassified kernel density raster
kernel_density_reclass = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Kernel_Density_Reclass"

arcpy.ddd.Contour(kernel_density_reclass, 
arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Contour_Density", 1, 0, 1, "CONTOUR_POLYGON", None)

density_polygon = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/Contour_Density"

arcpy.management.CopyFeatures(density_polygon, 
                              arcpy.env.workspace + "/Crimes_Density_Polygon.shp", 
                              '', None, None, None)









