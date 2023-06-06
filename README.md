# air-quality
Acquiring and assessing air quality data from the city of Eindhoven.

## Data Handling
data acquisition from AiREAS & RIVM.
 ### Download from airboxes
Use python to download JSON format data through the airbox API.After the data downloaded, I observed that for the stations (id number:10,15,18,32,33,38), the 
data is empty, Before conver to CSV,I removed these empty files. Full code refer to download_data.py
 ### Download from RIVM
At the RIVM website, use time period 1/1/2019-31/1/2019 as filter, choose the two locations contain Eindhoven to download two csv data
 ### Upload data from airboxes
Convert the format of download files from JSON to CSV by python. 
In python, I loop over all the python files,read the needed keys and values from JSON then write them into the CSV file.
Full code refer to Convert.py
Create a table and upload CSV into the database by python 
Python code consist of three parts:
1. Connect database
2. Create table
Before creating a table, I observed the original data and the possibility of the data type of each column in CSV.
3. Upload data by psycopg2
In this part, when the data is conflicts with the data type of the corresponding field in the table. I gradually change the data type of the field until it could be successfully uploaded 
to the database.
4. Create primary key of the table
Full code refer to upload_airbox.py
 ### Upload data from RIVM
Full code refer to upload_rivm.py. the logic is similar to upload_airbox.py


### Extract data from database
Because the measurement interval is different in airbox and RIVM, I use the following sql to join two tables together and export from the database as CSV file.
```
create view airbox37 as select * from s2276895.airbox where airbox_id='37';
create view airbox39 as select * from s2276895.airbox where airbox_id='39';
create view air39noordjoin as SELECT a.*, r.waarde as NO2_RIVM ,r.locatie FROM airbox39 a, 
rivmnoordno2 r WHERE a.date = r.tijdstip;
create view air37Genojoin as SELECT a.*, r.waarde as NO2_RIVM ,r.locatie FROM airbox37 a, 
rivmgeoveno2 r WHERE a.date = r.tijdstip;
```
I calculated the hourly and daily average NO2 value by SQL as followings:
```
create table airboxday37
SELECT
 no2 , date_trunc('day',date) date
From s2276895.airbox37
create table airboxdayly37
as
SELECT
 AVG(no2) no2, date
From s2276895.airboxday37
group by date
```
the logic is similar to calculate the hourly and daily average value for aixbox 39 and RIVM data. After creating the daily and hourly tables. I joined the aixbox data table and rivm data 
table by the date.
## Exploratory data analysis (EDA) 
PM10 and PM2.5 from station 37 of Airbox to compare. These two pollutants have similar distributions. From the hist, boxplot and QQ plot, we could see that the distributions are asymmetric.
The red line is mean value and green line is median in plots. Both are positive skewed because the mean is larger than the median in the hist and boxplot. It could also see from the QQ plot. The whole curve is above the straight line
![air quality in January](https://github.com/XiaoyuSun-hub/air-quality/blob/master/exploreData/3e_a_line.png)

After log transformation, we could see from the graphs below. The distributions become symmetric and almost normal distributions.

![air quality in January](https://github.com/XiaoyuSun-hub/air-quality/blob/master/exploreData/3a_2.png)

## Build linear regression of RIVM NO2 and airbox NO2 and make prediction. 

## Visualization through ArcMap and Tableau
### the air pollutants trend for January 2019.
![air quality in January](https://github.com/XiaoyuSun-hub/air-quality/blob/master/visualizedata/graph1.png)
the NO2, PM10, PM2.5 measurements from the airbox data are showed in the picture.  the date unit day as the x and different 
pollutants value as y. This graph shows the temporal character of the pollutants. We could see that these polutants have similar trends for the January.
### the air pollutants at each station for January 2019
![air quality in January](https://github.com/XiaoyuSun-hub/air-quality/blob/master/visualizedata/graph3.png)
the NO2, PM10, PM2.5 measurements from the airbox data are showed in the picture.  the date unit day as the x and different pollutants value as y. This bar graph allows us compare pollutants between airbox stations.Because the station id is related to the location, we could relate the pollutants to the location. From the bar graph we could see at airbox 30, the NO2 is highest among them. We could conclude that pollution is severe at the location of the airbox 30.
### Monthly Mean PM2.5 At Airbox Measurement Stations For January 2019 In Eindhoven
![air quality of PM2.5](https://github.com/XiaoyuSun-hub/air-quality/blob/master/visualizedata/point.png)
a thematic map in ArcMap to show the monly mean value of PM2.5 for January 2019. I combine size and value to display the PM2.5. Because the measurements are quantitative, ratio and relative.The dark value shows the high value, and light value shows the low value .Big size means high value and small size means small value.The relation between the symbol size and quantity size fits our intuition.
Monthly Mean PM2.5 IDW Interpolate Map for January 2019 In Eindhoven
![air quality of PM2.5](https://github.com/XiaoyuSun-hub/air-quality/blob/master/visualizedata/pollutant_idw.png)
the PM 2.5 pollution interpolate map created in ArcMap by using IDW interpolate. The number is the station id. I classify the density into five classes and use the value to display them. The dark value shows the high value and light value show low value which fits our intuition.

