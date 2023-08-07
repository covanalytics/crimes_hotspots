

source("r_files/package_load.R")

#///////////////////////////////////////////////////////////////////////////////////
## connect to historical database----
#///////////////////////////////////////////////////////////////////////////////////
cons.police <- dbConnect(drv=RSQLite::SQLite(), dbname=db_dir)


#////////////////////////////////////////////////////////////////////
#### Add .csv to filenames --------------
#////////////////////////////////////////////////////////////////////

#Files from Google Drive do not have the '.csv' suffix. 
#The suffix is added to the name and the updated files are loaded
police_24drive <- paste(drive_dir, "Police/24_hr_shift_report/download", sep = "")

oldNames<-list.files(police_24drive, full.names = TRUE) 
newNames<-paste(oldNames,".csv", sep="")
for (i in 1:length(oldNames)) file.rename(oldNames[i],newNames[i])

#Create a character vector of all EXCEL files with the '.csv'
filenames <- list.files(path = police_24drive, pattern=".csv", full.names=T)

#Read the contents of all EXCEl worksheets into a list
df.lists  <- lapply(filenames, function(x) read.csv(file=x, header=TRUE, stringsAsFactors = FALSE))

#Bind the rows of the data.frame lists created from the EXCEL sheets
daily_24hr  <- rbind.fill(df.lists)
daily_24hr$Date2 <- ""
names(daily_24hr) <- names(burgs_hist)

#//////////////////////////////////////////////////////////////////////////////
### Burglaries ----------------
#/////////////////////////////////////////////////////////////////////////////

burgs_hist <- dbGetQuery(cons.police, "SELECT * FROM Weekly_Hot_Spot WHERE [Incident Type] == 'Burglary'")
burgs_hist <- burgs_hist[, c(1:10)]
burgs_hist$Date <- ymd(burgs_hist$Date)

burgs_hist$Date2 <- ymd_hms(burgs_hist$Date2)


##! Keep only distinct burglary calls by incident number and with the first responding unit !##
daily_burgs <- daily_24hr %>%
  #bind_rows(jan_burg)%>%
  filter(grepl("Burglary", `Incident Type`))%>%
  group_by(IncidentNu, `Incident Type`, Address, Lat, Lon)%>%
  filter(row_number()==1) %>%
  mutate(Lat = as.numeric(Lat), 
         Lon = as.numeric(Lon),
         Date = mdy_hms(Date),
        Date2 = Date)%>% 
  bind_rows(burgs_hist)%>%
  #field must be a date for space time cube)%>%
  mutate(Count = 1)
  daily_burgs_hist <- daily_burgs
  daily_burgs <- daily_burgs %>%
    filter(Date >= today() - days(110))
  
daily_burgs$Date<- format(strptime(daily_burgs$Date, format='%Y-%m-%d %H:%M:%S'), '%Y-%m-%d')
daily_burgs$Date <- ymd(daily_burgs$Date)
daily_burgs <- daily_burgs[!grepl("POLICE", daily_burgs$Address),]
#daily_burgs <- daily_burgs[!duplicated(daily_burgs),]
daily_burgs <- daily_burgs[!grepl("2023-00009449", daily_burgs$IncidentNu),]

## Export for datacube and emerging hot spot analysis ##
city_bndy <- st_read(geo_dir, "City_Covington")
city_bndy <- st_transform(city_bndy, crs = 4326)

burgs_sf <- st_as_sf(daily_burgs, coords = c("Lon", "Lat"),  crs = 4326)
burgs_sf <- st_join(burgs_sf, city_bndy, join = st_within)%>%
  filter(!is.na(CITY))

st_write(burgs_sf, 
         map_dir, 
         layer = "burglaries_daily", 
         driver = "ESRI Shapefile", 
         delete_layer = TRUE)


#////////////////////////////////////////////////////////////////////////////////////////////////////////
### Motor Vehicle Thefts ----------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////

auto_theft_hist <- dbGetQuery(cons.police, "SELECT * FROM Weekly_Hot_Spot 
                          WHERE [Incident Type] == 'Theft-Motor Vehicle' OR 
                         [Incident Type] == 'Theft - Motor Vehicle'")
auto_theft_hist <- auto_theft_hist[, c(1:10)]
auto_theft_hist$Date <- ymd(auto_theft_hist$Date)
auto_theft_hist$Date2 <- ymd_hms(auto_theft_hist$Date2)

##Filtering data
##! Keep only motor vehicle thefts calls by incident number and with the first responding unit !##
daily_vthefts <- daily_24hr %>%
  filter(grepl("Theft-Motor Vehicle", `Incident Type`))%>%
  group_by(IncidentNu, `Incident Type`, Address, Lat, Lon)%>%
  filter(row_number()==1) %>%
  mutate(Lat = as.numeric(Lat), 
         Lon = as.numeric(Lon),
         Date = mdy_hms(Date),
         Date2 = Date)%>% 
  bind_rows(auto_theft_hist)%>%
  mutate(Count = 1)
daily_vthefts_hist <- daily_vthefts
  #field must be a date for space time cube)%>%
  daily_vthefts <- daily_vthefts %>%
    filter(Date >= today() - days(170))
  

daily_vthefts$Date<- format(strptime(daily_vthefts$Date, format='%Y-%m-%d %H:%M:%S'), '%Y-%m-%d')
daily_vthefts$Date <- ymd(daily_vthefts$Date)
daily_vthefts <- daily_vthefts[!grepl("POLICE", daily_vthefts$Address),]
daily_vthefts$`Incident Type` <- gsub(" - ", "-", daily_vthefts$`Incident Type`)
#daily_vthefts$Date <- as.character(daily_vthefts$Date)

## Export for datacube and emerging hot spot analysis ##
thefts_sf <- st_as_sf(daily_vthefts, coords = c("Lon", "Lat"),  crs = 4326)
thefts_sf <- st_join(thefts_sf, city_bndy, join = st_within)%>%
  filter(!is.na(CITY))

st_write(thefts_sf, 
         map_dir, 
         layer = "vehicle_thefts_daily", 
         driver = "ESRI Shapefile", 
         delete_layer = TRUE)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////
### Robberies ----------------
#////////////////////////////////////////////////////////////////////////////////////////////////////////////

robbery_hist <- dbGetQuery(cons.police, "SELECT * FROM Weekly_Hot_Spot 
                           WHERE [Incident Type] == 'Robbery'")
robbery_hist <- robbery_hist[, c(1:10)]
robbery_hist$Date <- ymd(robbery_hist$Date)
robbery_hist$Date2 <- ymd_hms(robbery_hist$Date2)

##Filtering data
##! Keep only distinct robbery calls by incident number and with the first responding unit !##
daily_robs <- daily_24hr %>%
  filter(grepl("Robbery", `Incident Type`))%>%
  group_by(IncidentNu, `Incident Type`, Address, Lat, Lon)%>%
  filter(row_number()==1) %>%
  mutate(Lat = as.numeric(Lat), 
         Lon = as.numeric(Lon),
         Date = mdy_hms(Date),
        Date2 = Date)%>% 
  bind_rows(robbery_hist)%>%
  mutate(Count = 1)
  daily_robs_hist <- daily_robs
  #field must be a date for space time cube)%>%
  daily_robs <- daily_robs %>%
    filter(Date >= today() - days(720))
  

daily_robs$Date<- format(strptime(daily_robs$Date, format='%Y-%m-%d %H:%M:%S'), '%Y-%m-%d')
daily_robs$Date <- ymd(daily_robs$Date)
daily_robs <- daily_robs[!grepl("POLICE", daily_robs$Address),]
#daily_robs$Date <- as.character(daily_robs$Date)
#daily_robs$Date <- ymd_hms(daily_robs$Date)
daily_robs$Lon[grepl("11/GREENUP", daily_robs$Address)] <- -84.508415 
daily_robs$Lat[grepl("11/GREENUP", daily_robs$Address)] <- 39.089944

## Export for datacube and emerging hot spot analysis ##
robs_sf <- st_as_sf(daily_robs, coords = c("Lon", "Lat"),  crs = 4326)
robs_sf <- st_join(robs_sf, city_bndy, join = st_within)%>%
  filter(!is.na(CITY))

st_write(robs_sf, 
         map_dir, 
         layer = "robberies_daily", 
         driver = "ESRI Shapefile", 
         delete_layer = TRUE)

#//////////////////////////////////////////////////////////////////////////////////////////
### Theft from Motor Vehicle ----------------
#/////////////////////////////////////////////////////////////////////////////////////////
theft_hist <- dbGetQuery(cons.police, "SELECT * FROM Weekly_Hot_Spot 
                           WHERE [Incident Type] == 'Theft-From a Motor Vehicle'")
theft_hist <- theft_hist[, c(1:10)]
theft_hist$Date <- ymd(theft_hist$Date)
theft_hist$Date2 <- ymd_hms(theft_hist$Date2)

##Filtering data
##! Keep only distinct theft from motor vehicle calls by incident number and with the first responding unit !##
daily_theft <- daily_24hr %>%
  filter(grepl("Theft-From a Motor Vehicle", `Incident Type`))%>%
  group_by(IncidentNu, `Incident Type`, Address, Lat, Lon)%>%
  filter(row_number()==1) %>%
  mutate(Lat = as.numeric(Lat), 
         Lon = as.numeric(Lon),
         Date = mdy_hms(Date),
         Date2 = Date)%>%
  bind_rows(theft_hist)%>%
  mutate(Count = 1)
daily_theft_hist <- daily_theft
  #field must be a date for space time cube)%>%
  daily_theft <- daily_theft %>%
    filter(Date >= today() - days(220))
  

daily_theft$Date<- format(strptime(daily_theft$Date, format='%Y-%m-%d %H:%M:%S'), '%Y-%m-%d')
daily_theft$Date <- ymd(daily_theft$Date)
daily_theft <- daily_theft[!grepl("POLICE", daily_theft$Address),]
daily_theft$`Incident Type` <- gsub(" - ", "-", daily_theft$`Incident Type`)


## Export for datacube and emerging hot spot analysis ##
vehicle_sf <- st_as_sf(daily_theft, coords = c("Lon", "Lat"),  crs = 4326)
vehicle_sf <- st_join(vehicle_sf, city_bndy, join = st_within)%>%
  filter(!is.na(CITY))

st_write(vehicle_sf, 
         map_dir, 
         layer = "thefts_from_vehicle_daily", 
         driver = "ESRI Shapefile", 
         delete_layer = TRUE)

#/////////////////////////////////////////////////////////////////////////////////////////////////
#### Criminal Mischief of Automobiles----
#////////////////////////////////////////////////////////////////////////////////////////////////

#special report created by KC dispatch to link criminal mischief of auto to call id
#this report links to other data systems outside of dispatch

##Reading in the data
mischief_auto <- paste(drive_dir, "Police/24_hr_shift_report/criminal_mischief_auto", sep = "")

#Create a character vector of all EXCEL files
a_filenames <- list.files(path = mischief_auto, pattern=".csv", full.names=T)

#Read the contents of all EXCEl worksheets into a list
#assign the next largest number to the most recent report
a_mischief_auto <- read.csv(max(a_filenames), header = TRUE, stringsAsFactors = FALSE)

names(a_mischief_auto)[1] <- "IncidentNu"


## Load the historical data
misch_hist <- dbGetQuery(cons.police, "SELECT * FROM Weekly_Hot_Spot  
                         WHERE [Incident Type] == 'Criminal Mischief-Auto'")


misch_hist <- misch_hist[, c(1:10)]

misch_hist$Date <- ymd(misch_hist$Date)
misch_hist$Date2 <- ymd_hms(misch_hist$Date2)
misch_hist$Count <- 1


##! Keep only distinct criminal mischief of auto calls by incident number and with the first responding unit !##
daily_mischief <- daily_24hr %>%
  #filter(grepl("Criminal Mischief", `Incident Type`))%>%
  group_by(IncidentNu, `Incident Type`, Address, Lat, Lon)%>%
  filter(row_number()==1) %>%
  mutate(Lat = as.numeric(Lat), 
         Lon = as.numeric(Lon),
         Date = mdy_hms(Date),
         Date2 = Date)%>%
  bind_rows(misch_hist)%>%
  left_join(a_mischief_auto, by = "IncidentNu")%>%
  filter(!is.na(Case.ORI) | `Incident Type` == "Criminal Mischief-Auto")%>%
  #distinct()%>%
  mutate(`Incident Type` = "Criminal Mischief-Auto")%>%
  select(1:10)%>%
  mutate(Count = 1)
daily_mischief_hist <- daily_mischief
#field must be a date for space time cube)%>%
daily_mischief <- daily_mischief %>%
  filter(Date >= today() - days(320))


daily_mischief$Date<- format(strptime(daily_mischief$Date, format='%Y-%m-%d %H:%M:%S'), '%Y-%m-%d')
daily_mischief$Date <- ymd(daily_mischief$Date)
daily_mischief <- daily_mischief[!grepl("POLICE", daily_mischief$Address),]
daily_mischief$`Incident Type` <- gsub(" - ", "-", daily_mischief$`Incident Type`)

#daily_robs$Date <- ymd_hms(daily_robs$Date)

## Export for datacube and emerging hot spot analysis ##
mischief_sf <- st_as_sf(daily_mischief, coords = c("Lon", "Lat"),  crs = 4326) %>%
  st_join(city_bndy, join = st_within)%>%
  filter(!is.na(CITY))

st_write(mischief_sf, 
         map_dir, 
         layer = "vehicle_mischief_daily", 
         driver = "ESRI Shapefile", 
         delete_layer = TRUE)


#/////////////////////////////////////////////////////////////////////////////////////////
### Combine historical files containing recent update----
#/////////////////////////////////////////////////////////////////////////////////////////

daily_burgs_hist <- daily_burgs_hist[!grepl("2023-00009449", daily_burgs_hist$IncidentNu),]
weekly_data_update <- rbind(daily_burgs_hist, 
                            daily_vthefts_hist,
                            daily_robs_hist, 
                            daily_theft_hist, 
                            daily_mischief_hist)

weekly_data_update <- weekly_data_update %>%
  mutate(Date = as.character(Date),
         Date2 = as.character(Date2),
         Date = format(strptime(Date, format = '%Y-%m-%d %H:%M:%S'), '%Y-%m-%d'))


weekly_data_update$Date <- as.character(weekly_data_update$Date)
weekly_data_update$Date2 <- as.character(weekly_data_update$Date2)
weekly_data_update$Date<- format(strptime(weekly_data_update$Date, format='%Y-%m-%d %H:%M:%S'), '%Y-%m-%d')

#///////////////////////////////////////////////////////////////////////////////////////////
### Overwrite historical database with new data----
#//////////////////////////////////////////////////////////////////////////////////////////
library("RSQLite")
cons.police <- dbConnect(drv=RSQLite::SQLite(), dbname=db_dir)
dbWriteTable(cons.police, "Weekly_Hot_Spot", weekly_data_update, overwrite = TRUE)
crimes <- dbGetQuery(cons.police, 'select * from Weekly_Hot_Spot')
dbDisconnect(cons.police)







