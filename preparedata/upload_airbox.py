import psycopg2
from os import listdir,getcwd
from os.path import isfile, join
'''

'''
conn = psycopg2.connect(host="", dbname="", port="", user="",password="")
cur = conn.cursor()
'''
cur.execute(
    """
    Drop table 5.airbox1
    """
)
conn.commit()
'''
#create table
cur.execute("""
CREATE TABLE 5.airbox
(
    airbox_id integer,
    AmbHum double precision,
    PM1 double precision,
    WBGT double precision,
    UFP double precision,
    PM25 double precision,
    Ozon double precision,
    PM10 double precision,
    Temp double precision,
    RelHum double precision,
    AmbTemp double precision,
    NO2 double precision,
    GPS_lat double precision,
    GPS_lon double precision,
    date timestamp 
)
""")
conn.commit()
#batch copy csv files into the database
path= getcwd()
mypath = path+'\\airbox\\csv'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for f in onlyfiles:
    with open(join(mypath, f), 'r') as f:
     next(f) # Skip the header row.
     cur.copy_from(f, 'airbox', sep=',')
    conn.commit()
    print(f)
#create and set primary key
cur.execute(
    """
    ALTER TABLE 5.airbox
  ADD id  SERIAL PRIMARY KEY
    """
)
conn.commit()
