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

``` python
theft_cube = arcpy.env.workspace + "/vtheft_cube_weekly.nc"
arcpy.stpm.CreateSpaceTimeCube(theft_prj, 
                               theft_cube,
                               "Date",
                               None, 
                               "1 Weeks", 
                               "END_TIME", 
                               None, 
                               "300 Feet", 
                               "Count SUM ZEROS", 
                               "HEXAGON_GRID", None, None)
```

### Creating Emerging Hotspots

