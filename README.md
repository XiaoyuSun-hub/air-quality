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
Upload data from RIVM
Full code refer to upload_rivm.py. the logic is similar to upload_airbox.py

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

## Visualization through ArcMap and Tableau
！

