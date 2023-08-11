
source("r_files/package_load.R")



#////////////////////////////////////
##1. Snapshot--Prepare Crimes for Mapping----
#///////////////////////////////////
city <- st_read(geo_dir, "City_Covington")
city_sf <- st_transform(city, crs = 4326)
police <- st_read(paste(map_dir, "police_sectors.shp", sep="/"))
police_sf <- st_transform(police, crs = 4326)
neigh <- st_read(geo_dir, "Neighborhoods_Covington")
neigh_sf <- st_transform(neigh, crs = 4326)


crimes1<- rbind(burgs_sf, thefts_sf, robs_sf, vehicle_sf, mischief_sf)%>%
  st_transform(crs = 4326)%>%
  select(1:10)%>%
  st_join(neigh_sf, join = st_within)%>%
  #filter (Date >= today() - days(31))%>%
  #mutate(`Incident Type` = as.factor(`Incident Type`))%>%
  select(1:10,14)

st_write(crimes1, 
         map_dir, 
         layer = "crimes", 
         driver = "ESRI Shapefile", 
         delete_layer = TRUE)
crimes <- st_join(crimes1, police_sf, join = st_within)%>%
    filter (Date >= today() - days(31))
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
crimes_df$`Incident Type`[crimes_df$`Incident Type` == 'Criminal Mischief-Auto'] <- "CM Auto"

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
  ylim(c(0,20))+
  
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

ggsave(paste(map_dir, "/crime_snapshot_", 
             today(), 
             ".png", 
             sep = ""), crime_snap, width = 8, height = 7, units = "in", dpi = 120)



crimes <- st_read("U:/Mapping/Police/Crimes.shp")
crimes_sf <- st_transform(crimes, crs = 4326)%>%
  filter(!grepl("South Covington", NbhdLbl))

saveRDS(crimes_sf, "C:/Users/tsink/Documents/covdata_graphics/data/police/crimes.rds")

density <- st_read("C:/Users/tsink/Documents/ArcGIS/Projects/Weekly_Crime_Hotspot/Crimes_Density_Polygon.shp")
density_sf <- st_transform(density, crs = 4326) %>%
  filter(ContourMin > 1)

saveRDS(density_sf, "C:/Users/tsink/Documents/covdata_graphics/data/police/crimes_density.rds")



