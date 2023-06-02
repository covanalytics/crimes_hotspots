
source("r_files/package_load.R")



cons.police <- dbConnect(drv=RSQLite::SQLite(), dbname=db_dir)
#dbWriteTable(cons.police, "Weekly_Hot_Spot", burgs_hist, overwrite = TRUE )
burgs_hist <- dbGetQuery(cons.police, "SELECT * FROM Weekly_Hot_Spot WHERE [Incident Type] == 'Burglary'")
burgs_hist <- burgs_hist[, c(1:10)]
burgs_hist$Date <- ymd(burgs_hist$Date)
#burgs_hist$Date <- as.character(burgs_hist$Date)
burgs_hist$Date2 <- ymd_hms(burgs_hist$Date2)
#burgs_hist <- burgs_hist[!grepl("Robbery", burgs_hist$`Incident Type`),]
#burgs_hist$Count <- 1


##Reading in the data
police_24drive <- paste(drive_dir, "Police/24_hr_shift_report/download", sep = "")

oldNames<-list.files(police_24drive, full.names = TRUE) 
newNames<-paste(oldNames,".csv", sep="")
for (i in 1:length(oldNames)) file.rename(oldNames[i],newNames[i])

#Create a character vector of all EXCEL files
filenames <- list.files(path = police_24drive, pattern=".csv", full.names=T)

#Read the contents of all EXCEl worksheets into a list
df.lists  <- lapply(filenames, function(x) read.csv(file=x, header=TRUE, stringsAsFactors = FALSE))

#Bind the rows of the data.frame lists created from the EXCEL sheets
daily_24hr  <- rbind.fill(df.lists)
daily_24hr$Date2 <- ""
names(daily_24hr) <- names(burgs_hist)

#daily_24hr <- jan_burg
### Burglaries ----------------
##Filtering data
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
  #filter(year(Date) >= 2022)%>%
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



### Motor Vehicle Thefts ----------------
auto_theft_hist <- dbGetQuery(cons.police, "SELECT * FROM Weekly_Hot_Spot WHERE [Incident Type] == 'Theft-Motor Vehicle' OR 
                         [Incident Type] == 'Theft - Motor Vehicle'")
auto_theft_hist <- auto_theft_hist[, c(1:10)]
auto_theft_hist$Date <- ymd(auto_theft_hist$Date)
auto_theft_hist$Date2 <- ymd_hms(auto_theft_hist$Date2)

##Filtering data
##! Keep only distinct burglary calls by incident number and with the first responding unit !##
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
  #filter(year(Date) >= 2022)%>%
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


### Robberies ----------------
robbery_hist <- dbGetQuery(cons.police, "SELECT * FROM Weekly_Hot_Spot WHERE [Incident Type] == 'Robbery'")
robbery_hist <- robbery_hist[, c(1:10)]
robbery_hist$Date <- ymd(robbery_hist$Date)
robbery_hist$Date2 <- ymd_hms(robbery_hist$Date2)

##Filtering data
##! Keep only distinct burglary calls by incident number and with the first responding unit !##
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
  #filter(year(Date) >= 2022)%>%
  daily_robs <- daily_robs %>%
    filter(Date >= today() - days(720))
  

#daily_robs$Date<- format(strptime(daily_robs$Date, format='%Y-%m-%d %H:%M:%S'), '%Y-%m-%d')
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


### Theft from Motor Vehicle ----------------
theft_hist <- dbGetQuery(cons.police, "SELECT * FROM Weekly_Hot_Spot 
                           WHERE [Incident Type] == 'Theft-From a Motor Vehicle'")
theft_hist <- theft_hist[, c(1:10)]
theft_hist$Date <- ymd(theft_hist$Date)
theft_hist$Date2 <- ymd_hms(theft_hist$Date2)

##Filtering data
##! Keep only distinct burglary calls by incident number and with the first responding unit !##
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
  #filter(year(Date) >= 2022)%>%
  daily_theft <- daily_theft %>%
    filter(Date >= today() - days(220))
  

daily_theft$Date<- format(strptime(daily_theft$Date, format='%Y-%m-%d %H:%M:%S'), '%Y-%m-%d')
daily_theft$Date <- ymd(daily_theft$Date)
daily_theft <- daily_theft[!grepl("POLICE", daily_theft$Address),]
daily_theft$`Incident Type` <- gsub(" - ", "-", daily_theft$`Incident Type`)

#daily_robs$Date <- ymd_hms(daily_robs$Date)

## Export for datacube and emerging hot spot analysis ##
vehicle_sf <- st_as_sf(daily_theft, coords = c("Lon", "Lat"),  crs = 4326)
vehicle_sf <- st_join(vehicle_sf, city_bndy, join = st_within)%>%
  filter(!is.na(CITY))

st_write(vehicle_sf, 
         map_dir, 
         layer = "thefts_from_vehicle_daily", 
         driver = "ESRI Shapefile", 
         delete_layer = TRUE)



daily_burgs_hist <- daily_burgs_hist[!grepl("2023-00009449", daily_burgs_hist$IncidentNu),]
weekly_data_update <- rbind(daily_burgs_hist, daily_vthefts_hist, daily_robs_hist, daily_theft_hist)
weekly_data_update$Date <- as.character(weekly_data_update$Date)
weekly_data_update$Date2 <- as.character(weekly_data_update$Date2)
weekly_data_update$Date<- format(strptime(weekly_data_update$Date, format='%Y-%m-%d %H:%M:%S'), '%Y-%m-%d')


library("RSQLite")
cons.police <- dbConnect(drv=RSQLite::SQLite(), dbname=db_dir)
dbWriteTable(cons.police, "Weekly_Hot_Spot", weekly_data_update, overwrite = TRUE)
crimes <- dbGetQuery(cons.police, 'select * from Weekly_Hot_Spot')
dbDisconnect(cons.police)



#////////////////////////////////////
##1. Snapshot--Prepare Crimes for Mapping----
#///////////////////////////////////
city <- st_read(geo_dir, "City_Covington")
city_sf <- st_transform(city, crs = 4326)
police <- st_read(paste(map_dir, "police_sectors.shp", sep=""))
police_sf <- st_transform(police, crs = 4326)
neigh <- st_read(geo_dir, "Neighborhoods_Covington")
neigh_sf <- st_transform(neigh, crs = 4326)


crimes1<- rbind(burgs_sf, thefts_sf, robs_sf, vehicle_sf)%>%
  st_transform(crs = 4326)%>%
  select(1:10)%>%
  st_join(neigh_sf, join = st_within)%>%
  filter (Date >= today() - days(31))%>%
  #mutate(`Incident Type` = as.factor(`Incident Type`))%>%
  select(1:10,14) 
crimes <- st_join(crimes1, police_sf, join = st_within)
#crimes$`Incident Type` <- as.factor(crimes$`Incident Type`)
crimes$Hour <- format(strptime(crimes$Date2, format='%Y-%m-%d %H:%M:%S'), '%I %p')
crimes$Hour_AM_PM <- format(strptime(crimes$Date2, format='%Y-%m-%d %H:%M:%S'), '%p')
hour_level <- c('12 AM', '01 AM', '02 AM', '03 AM', '04 AM', '05 AM', '06 AM', '07 AM', '08 AM', '09 AM',
                '10 AM', '11 AM', '12 PM', '01 PM', '02 PM', '03 PM', '04 PM', '05 PM',
                '06 PM', '07 PM', '08 PM', '09 PM', '10 PM', '11 PM')

crimes_df <- as.data.frame(crimes)
crimes_df <- crimes_df %>%
  mutate(Hour = factor(crimes$Hour, levels = hour_level))

crimes_df <- crimes_df %>%
mutate(lat = unlist(map(crimes$geometry,2)),
       lon = unlist(map(crimes$geometry,1)))

crimes_df$`Incident Type`[crimes_df$`Incident Type` == 'Theft-From a Motor Vehicle'] <- "Theft From MV"
crimes_df$`Incident Type`[crimes_df$`Incident Type` == 'Theft-Motor Vehicle'] <- "Theft of MV"


##//////////////////////////////////////##
##2. Snapshot--Heat map crimes by Type ----
##//////////////////////////////////////##
crimes_heat <- crimes_df %>%
  filter(!grepl("South Covington", NbhdLabel))

#max_lon <- max(crimes_heat$lon)+ 0.05
#min_lon <- min(crimes_heat$lon)- 0.05

#max_lat <- max(crimes_heat$lat)+ 0.01
#min_lat <- min(crimes_heat$lat)- 0.01

crime_hotspot <- qmplot(lon, lat, data = crimes_heat, geom = "blank", zoom = 14, darken = .2)+
  #geom_density_2d_filled(contour_var = "ndensity")+
  #scale_x_continuous(limits = c(min_lon, max_lon), expand = c(0, 0)) +
  #scale_y_continuous(limits = c(min_lat, max_lat), expand = c(0, 0)) +
  stat_density_2d(aes(fill = ..level..), 
                  geom = "polygon", 
                  alpha = .40,
                  bins = 2,
                  adjust = 2/3, color = "black", 
                  contour_var = "ndensity")+#maintain peak density across facets.Remove to show varation across groups
  #scale_fill_gradient2("Density", low = "blue", mid = "yellow", high = "red")+
  #scale_fill_gradient2("Density", low = "black", high = "red")+
  scale_fill_gradient2("Density", low = "black", high = "red")+
  #scale_alpha(range = c(0, 0.75)) +  
  facet_wrap(~ `Incident Type`, nrow = 1)+
  
  geom_point(coinherit.aes = TRUE, size = 0.6)+
  
  geom_sf(data = police_sf, fill = NA, lwd = 0.2, color = "black", inherit.aes = FALSE)+
  
  
  ggtitle("Crimes Reported--Last 30 Days")+
  theme_bw()+
  theme(axis.text.x = element_blank(), 
        axis.text.y = element_blank(),
        axis.ticks = element_blank(),
        axis.title = element_blank(),
        plot.title = element_text(hjust = 0.5, size = 16, color = "black", face = "bold"),
        strip.text = element_text(size = 8, face = "italic"),
        legend.position = "none",
        legend.text = element_blank(),
        legend.box.background = element_rect(color = "black", size = 1))
        #panel.border = element_rect(color = "black", fill=NA, size=1),
        #plot.background = element_rect(color = "black", size = 1))
  #labs(caption = paste(today(), "City of Covington", sep = "\n"))
#ggsave(paste("U:/Mapping/Police/crime_hot_spots_type_", today(), ".png", sep = ""), crime_hotspot)

#///////////////////////////////////////////////////////////// 
###3. Snapshot--Bar Chart by AM/PM----
#/////////////////////////////////////////////////////////////
crimes_ampm <- crimes_df %>%
  group_by(Hour_AM_PM)%>%
  summarise(Count = sum(Count))%>%
  ggplot(aes(x=Hour_AM_PM, y = Count, fill = Hour_AM_PM))+
  geom_bar(stat = 'identity')+
 
  theme_bw()+
  scale_fill_manual(values=c('#c3b632','#3d134f'))+
  ylim(c(0,80))+
  labs(caption = paste("","", "Weekly snapshot", 
                       today(), 
                       "City of Covington", sep = "\n"))+
  #scale_x_continuous(limits = c(0, 30))+
  geom_text(aes(label=Count),  position= "identity", vjust = -1.0, size = 2.7)+
  
  theme(strip.text = element_text(size = 12, face = "italic"),
        legend.position = "bottom",
        legend.title = element_blank(),
        axis.title = element_blank(),
        panel.border = element_rect(color = "black", fill=NA, size=0.5),
        plot.caption = element_text(hjust = 0, face = "italic", size = 10))
#///////////////////////////////////////////////////////////// 
###3.1 Snapshot--Bar Chart by Beat----
#/////////////////////////////////////////////////////////////
crimes_beat <- crimes_df %>%
  group_by(BEAT, Hour_AM_PM)%>%
  summarise(Count = sum(Count))%>%
  ggplot(aes(x=BEAT, y = Count, fill = Hour_AM_PM, group = Hour_AM_PM))+
  geom_bar(stat = 'identity', position = "dodge")+
  #facet_wrap(~BEAT)+
  
  theme_bw()+
  scale_fill_manual(values=c('#c3b632','#3d134f'))+
  ylim(c(0,20))+
  #labs(caption = paste("","", "Weekly snapshot of crimes reported in last 30 days", 
                       #today(), 
                       #"City of Covington", sep = "\n"))+
  #scale_x_continuous(limits = c(0, 30))+
  geom_text(aes(label=Count),  position= position_dodge(0.9), vjust = -1.0, size = 2.7)+
  
  theme(legend.position = "none",
        legend.title = element_blank(),
        axis.title.y = element_blank(),
        #axis.title = element_blank(),
        panel.border = element_rect(color = "black", fill=NA, size=0.5),
        plot.caption = element_text(hjust = 0, face = "italic", size = 10))

#///////////////////////////////////////////////////////////// 
###4. Snapshot--Bar Chart by AM/PM and Incident Type----
#/////////////////////////////////////////////////////////////
crimes_ampm_bchrt <- crimes_df %>%
  group_by(`Incident Type`, Hour_AM_PM)%>%
  summarise(Count = sum(Count))%>%
  #filter(Issued == "Pending")%>%
  ggplot(aes(x=`Incident Type`, y=Count, fill = Hour_AM_PM))+
  geom_bar(stat = 'identity', position = "dodge")+
  #facet_wrap(~TYPE)+
  scale_fill_manual(values=c('#c3b632','#3d134f'))+
  ylim(c(0,30))+
  
  #coord_flip()+
  geom_text(aes(label=Count),  position= position_dodge(0.9), vjust = -1.0, size = 2.7)+
  theme_bw()+
  theme(legend.position = "none",
        legend.title = element_blank(),
        axis.title = element_blank(),
        axis.text.x = element_text(size = 10, angle = 90, vjust = 0.5, hjust=1))
        


#///////////////////////////////////////////////////////////// 
###5. Snapshot--Combined Plots/Save PNG----
#/////////////////////////////////////////////////////////////
crime_snap <- ggarrange(crime_hotspot, 
                      ggarrange(crimes_ampm, crimes_beat, crimes_ampm_bchrt, ncol = 3), nrow = 2)

ggsave(paste("U:/Mapping/Police/crime_snapshot_", 
             today(), 
             ".png", 
             sep = ""), crime_snap, width = 672, height = 672, units = "px", dpi = 120)


#crime_snap <- ggarrange(crime_hotspot, crimes_ampm, crimes_beat,
                       # crimes_ampm_bchrt, ncol = 2, nrow = 2)
##//////////////////////////////////////##
##D-3 Heat map of all crimes ----
##//////////////////////////////////////##
all_crimes <- qmplot(lon, lat, data = crimes_df, geom = "blank", zoom = 14, darken = .3)+
  #geom_point(data = crimes_df, aes(x=lon, y=lat, fill= `Incident Type`), pch=21, size = 1.5, colour="black")+
  stat_density_2d(aes(fill = ..level..), 
                  geom = "polygon", 
                  alpha = .40,
                  bins = 4,
                  adjust = 2/3,  
                  contour_var = "count")+#maintain peak density across facets.Remove to show varation across groups
  #scale_fill_gradient2("Density", low = "blue", mid = "yellow", high = "red")+
  #scale_fill_gradient2("Density", low = "black", high = "red")+
  scale_fill_gradient("Density", low = "yellow", high = "red")+
  #scale_alpha(range = c(0, 0.75)) +  
  #facet_wrap(~ `Incident Type`, nrow = 2)+
  #geom_point(data = crimes_df, aes(x=lon, y=lat, fill = NbhdLabel), pch=21, size = 1.0, colour="black")+
  geom_point(coinherit.aes = TRUE,  size = 1.0)+
  
  geom_sf(data = police_sf, fill = NA, lwd = 0.5, color = "black", inherit.aes = FALSE)+
  
  ggtitle("All Crimes Density--All 4 Types")+
  theme_bw()+
  theme(axis.text.x = element_blank(), 
        axis.text.y = element_blank(),
        axis.ticks = element_blank(),
        axis.title = element_blank(),
        plot.title = element_text(hjust = 0.5, size = 16, color = "black", face = "bold"),
        strip.text = element_text(size = 12, face = "italic"),
        legend.position = "right",
        legend.text = element_blank(),
        legend.box.background = element_rect(color = "black", size = 1),
        panel.border = element_rect(color = "black", fill=NA, size=1),
        plot.background = element_rect(color = "black", size = 1))+
  labs(caption = paste(today(), "City of Covington", sep = "\n"))
ggsave(paste("U:/Mapping/Police/crime_hot_spots_", today(), ".png", sep = ""), all_crimes)

##//////////////////////////////////////##
##D-4 Heat map crimes by Hour of Day----
##//////////////////////////////////////##
hour_level <- c('12 AM', '01 AM', '02 AM', '03 AM', '04 AM', '05 AM', '06 AM', '07 AM', '08 AM', '09 AM',
                '10 AM', '11 AM', '12 PM', '01 PM', '02 PM', '03 PM', '04 PM', '05 PM',
                '06 PM', '07 PM', '08 PM', '09 PM', '10 PM', '11 PM')
crimes_df <- crimes_df %>%
  mutate(Hour = factor(crimes$Hour, levels = hour_level))

crimes_day_hour <- crimes_df %>%
  filter(!grepl("South Covington", NbhdLabel))
  qmplot(lon, lat, data = crimes_day_hour, geom = "blank", zoom = 14, darken = .3)+
  #geom_density_2d_filled(contour_var = "ndensity")+
  stat_density_2d(aes(fill = ..level..), 
                  geom = "polygon", 
                  alpha = .40,
                  bins = 4,
                  adjust = 1/3,
                  contour_var = "count")+#maintain peak density across facets.Remove to show varation across groups
  #scale_fill_gradient2("Density", low = "blue", mid = "yellow", high = "red")+
  #scale_fill_gradient2("Density", low = "black", high = "red")+
  scale_fill_gradient("Density", low = "yellow", high = "red")+
  #scale_alpha(range = c(0, 0.75)) +  
  facet_wrap(~ Hour, nrow = 3)+
  
  geom_point(coinherit.aes = TRUE, size = 1.0)+
  
  geom_sf(data = police_sf, fill = NA, lwd = 0.5, color = "black", inherit.aes = FALSE)+
  
  ggtitle("Crimes Density---Hour of Day")+
  theme_bw()+
  theme(axis.text.x = element_blank(), 
        axis.text.y = element_blank(),
        axis.ticks = element_blank(),
        axis.title = element_blank(),
        plot.title = element_text(hjust = 0.5, size = 16, color = "black", face = "bold"),
        strip.text = element_text(size = 12, face = "italic"),
        legend.position = "bottom",
        legend.text = element_blank(),
        legend.box.background = element_rect(color = "black", size = 1),
        panel.border = element_rect(color = "black", fill=NA, size=1),
        plot.background = element_rect(color = "black", size = 1))+
  labs(caption = paste(today(), "City of Covington", sep = "\n"))
ggsave(paste("U:/Mapping/Police/crime_hot_spots_DayHour_", today(), ".png", sep = ""), crimes_day_hour)

##//////////////////////////////////////##
##D-5 Heat map crimes by AM/PM----
##//////////////////////////////////////##

crimes_ampm <- qmplot(lon, lat, data = crimes_df, geom = "blank", zoom = 14, darken = .3)+
  #geom_density_2d_filled(contour_var = "ndensity")+
  stat_density_2d(aes(fill = ..level..), 
                  geom = "polygon", 
                  alpha = .40,
                  bins = 3,
                  adjust = 2/3,
                  contour_var = "ndensity")+#maintain peak density across facets.Remove to show varation across groups
  #scale_fill_gradient2("Density", low = "blue", mid = "yellow", high = "red")+
  #scale_fill_gradient2("Density", low = "black", high = "red")+
  scale_fill_gradient("Density", low = "yellow", high = "red")+
  #scale_alpha(range = c(0, 0.75)) +  
  #facet_wrap(~ Hour_AM_PM)+
  
  geom_point(coinherit.aes = TRUE, size = 1.0)+
  
  geom_sf(data = police_sf, fill = NA, lwd = 0.5, color = "black", inherit.aes = FALSE)+
  
  ggtitle("Crimes Density---AM / PM")+
  theme_bw()+
  theme(axis.text.x = element_blank(), 
        axis.text.y = element_blank(),
        axis.ticks = element_blank(),
        axis.title = element_blank(),
        plot.title = element_text(hjust = 0.5, size = 16, color = "black", face = "bold"),
        strip.text = element_text(size = 12, face = "italic"),
        legend.position = "bottom",
        legend.text = element_blank(),
        legend.box.background = element_rect(color = "black", size = 1),
        panel.border = element_rect(color = "black", fill=NA, size=1),
        plot.background = element_rect(color = "black", size = 1))+
  labs(caption = paste(today(), "City of Covington", sep = "\n"))
ggsave(paste("U:/Mapping/Police/crime_hot_spots_AM_PM_", today(), ".png", sep = ""), crimes_ampm)



library("magick")##image load
## city logo
city_logo <- image_read("U:/Mapping/city_logo.png")%>%
  image_resize(150)

#Load saved ggplot png, resize, add city seal, resize for emedding, then save
pub_plot <- image_read("U:/Mapping/Police/crime_hot_spots_2022-04-18.png")%>%
  image_resize(1500)%>% 
  image_composite(city_logo, offset = "+21+1900")
#image_resize(1500)

image_write(image = pub_plot, paste("U:/short_term_rentals_", today(), ".png", sep =""))





plot_height <- magick::image_info(pub_plot)$height
plot_width <- magick::image_info(pub_plot)$width

# get dims of the logo
logo_width <- magick::image_info(logo)$width
logo_height <- magick::image_info(logo)$height

# get number of pixels to be 1% from the bottom of the plot
# while accounting for the logo height
plot_height - logo_height - plot_height * 0.01

plot_width * 0.01

cov_gg +
  #geom_point(data = short_term, aes(x=lon, y=lat), color='black', size = 2)+
  #qmplot(lon, lat, data = short_term, geom = "blank", zoom = 14, darken = .3)+
  #geom_density_2d_filled(contour_var = "ndensity")+
  stat_density_2d(data = short_term, aes(x=lon, y=lat, fill = ..level..), 
                  geom = "polygon", 
                  alpha = .35, 
                  bins = 3, 
                  adjust = 2/3,  
                  contour_var = "count")+#maintain peak density across facets.Remove to show varation across groups
  scale_fill_gradient2("Density", low = "black", high = "red")+
  #scale_alpha(range = c(0, 0.75)) +  
  facet_wrap(~ TYPE)+
  
  geom_point(data = short_term, inherit.aes = TRUE, size = 1.5)+
  
  geom_sf(data = city_sf, fill = NA, lwd = 1, color = "black", inherit.aes = FALSE)+
  
  ggtitle("Short-Term Rentals")+
  theme_bw()+
  theme(axis.text.x = element_blank(), 
        axis.text.y = element_blank(),
        axis.ticks = element_blank(),
        axis.title = element_blank(),
        plot.title = element_text(hjust = 0.5, size = 16, color = "black", face = "bold"),
        strip.text = element_text(size = 12, face = "italic"),
        legend.position = "bottom",
        legend.text = element_blank(),
        legend.box.background = element_rect(color = "black", size = 1),
        panel.border = element_rect(color = "black", fill=NA, size=1),
        plot.background = element_rect(color = "black", size = 1))+
  labs(caption = paste(today()))



## Section 8 Heat Map Trial

library("RSQLite")
cons.sec8 <- dbConnect(drv=RSQLite::SQLite(), dbname="U:/Database Files/Section8.db")

sec8_hist <- dbGetQuery(cons.sec8, 'select * from History_2003_2021')
#write.csv(pending_extract, "pending_rentals.csv", row.names = FALSE)
dbDisconnect(cons.sec8)
sec8_hist$lat <- as.numeric(sec8_hist$lat)
sec8_hist$lon <- as.numeric(sec8_hist$lon)
sec8_hist_cov <- sec8_hist[(sec8_hist$NbhdLabel != "NA"),]
sec8_hist_cov <- sec8_hist_cov[sec8_hist_cov$NbhdLabel != "South Covington",]
qmplot(lon, lat, data = sec8_hist_cov, zoom = 13, geom = "blank",  darken = .3)+
  #geom_density_2d_filled(contour_var = "ndensity")+
  stat_density_2d(aes(fill = ..level..), 
                  geom = "polygon", 
                  alpha = .30, 
                  #bins = 10, 
                  adjust = 2/3, contour_var = "count")+#maintain peak density across facets.Remove to show varation across groups
  scale_fill_gradient2("Density", low = "black", high = "red")+
  #scale_alpha(range = c(0, 0.75)) +  
  facet_wrap(~ Year, nrow = 3)+
  
  #geom_point(inherit.aes = TRUE, size = 0.3)+
  
  geom_sf(data = city_sf, fill = NA, lwd = 1, color = "black", inherit.aes = FALSE)+
  
  ggtitle("Section 8 Participants: 2003-2021")+
  theme_bw()+
  theme(axis.text.x = element_blank(), 
        axis.text.y = element_blank(),
        axis.ticks = element_blank(),
        axis.title = element_blank(),
        plot.title = element_text(hjust = 0.5, size = 16, color = "black", face = "bold"),
        strip.text = element_text(size = 12, face = "italic"),
        legend.position = "bottom",
        legend.text = element_blank(),
        legend.box.background = element_rect(color = "black", size = 1),
        panel.border = element_rect(color = "black", fill=NA, size=1),
        plot.background = element_rect(color = "black", size = 1))+
  labs(caption = paste(today()))
ggsave("U:/r_section8.png")

#Load saved ggplot png, resize, add city seal, resize for emedding, then save
pub_plot <- image_read("U:/r_section8.png")%>%
  #image_resize(672)%>% 
  image_composite(city_logo, offset = "+21+1900")
#image_resize(1500)

image_write(image = pub_plot, paste("U:/section_8_", today(), ".png", sep =""))








