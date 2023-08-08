## README


<!-- TABLE OF CONTENTS -->
<details>
  <summary><b>Table of Contents</b></summary>
  <ol>
    <li><a href="#project">Project</a></li>
    <li><a href="#data-collection">Data Collection</a></li>
    <li><a href="#data-processing">Data Processing</a></li>
    <li><a href="#weekly-data-snapshot">Weekly Data Snapshot</a></li>
    <li><a href="#weekly-hotspot-models">Weekly Hotspot Models</a></li>
    <li><a href="#model-presentation">Model Presentation</a></li>
  </ol>
</details>


# Project


# Technology

-   Microsoft Power Automate
-   Google Drive
-   SQLite database engine
-   ArcGIS Pro
-   RStudio (64x bit needed to connect to library of tools in ArcGIS
    Pro)
-   ArcGIS Online

## R Packages

-   tidyverse
-   ggmap
-   sf
-   lubridate
-   ggpubr
-   arcgisbinding
-   RPyGeo (ArcGIS processing via Python)

# Data Collection

Every morning at 8:00 AM a shift report CSV containing the previous 24
hour police dispatches is received via automated email from the Kenton
County Kentucky Dispatch Center.

A Power Automate workflow was created to store the attached file in a Google Drive folder.

![](images/power_automate_overview.PNG)

# Data Processing

The daily 24 hour shift report files are processed in the R script
**daily_24hr_shift_report.R** The script reads, cleans, filters,
formats, and adds new features and stores new spatial data files that
are needed to generate hot spot models and weekly snapshots of crimes.

# Products Distributed

### Weekly Data Snapshot

Every week the Police Department receives a snapshot of crimes reported
over the last 30 days. The snapshot provides insight into where criminal
activities have been most concentrated and if they have occurred more
during the day or night.

The weekly snapshot is created in the R script **weekly_snapshot.R**

![](images/crime_snapshot_2023-08-08.png)

### Optimal and Emerging Hotspots

# Creating Hotspots

## ArcGIS Pro

We connect to the library of tools in ArcGIS Pro inside of Rstudio

``` r
arcpy <- rpygeo_build_env(path = "C:/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe", 
                          overwrite = TRUE,
                          extensions = "Spatial")
```

### Emerging Hotspots

Create space-time cube

``` python
theft_cube = arcpy.env.workspace + "/vtheft_cube_weekly.nc"
arcpy.stpm.CreateSpaceTimeCube(theft_prj,         #Projected shapefile
                               theft_cube,        #Data cube
                               "Date",            #Time field
                               None,              #Template cube
                               "1 Weeks",         #Time step interval
                               "END_TIME",        #Time step alignment; how aggregation occurs
                               None, 
                               "300 Feet",        #Size of bins to aggregate points
                               "Count SUM ZEROS", #Summary fields
                               "HEXAGON_GRID",    #The shape of the polygon mesh to aggregate points
                               None, None)
```

Analysis

``` python
theft_spot_path = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb/VTheft_Analysis_Emerging_HotSpot"
with arcpy.EnvManager(scratchWorkspace = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb", 
                      workspace = arcpy.env.workspace + "/Weekly_Crime_Hotspot.gdb"):
                      arcpy.stpm.EmergingHotSpotAnalysis(theft_cube, 
                      "COUNT_SUM_ZEROS", 
                       theft_spot_path, 
                       "300 Feet", 
                       1, None, "FIXED_DISTANCE", None, "ENTIRE_CUBE")
arcpy.management.CalculateField(theft_spot_path, "TYPE", '"Theft-Motor Vehicle"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")        
```

### Optimal Hotspots

