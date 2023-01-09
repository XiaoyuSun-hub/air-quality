import psycopg2
from os import listdir,getcwd
from os.path import isfile, join
'''
__5___

 
The port at which the server
listens to requests is port 
'''
conn = psycopg2.connect(host="", dbname="", port="", user="5",password="__5___")
cur = conn.cursor()
cur.execute(
    """
    Drop table 5.rivm
    """
)
conn.commit()
cur.execute("""
CREATE TABLE 5.rivm
(
     tijdstip timestamp,
     locatie  text,
    component text,
    waarde double precision,
    lki text
)
""")
conn.commit()
#id  SERIAL PRIMARY KEY
path= getcwd()
mypath = path+'\\rivm'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for f in onlyfiles:
    with open(join(mypath, f), 'r') as f:
    #Notice that we don't need the `csv` module.
     next(f) # Skip the header row.
     cur.copy_from(f, 'rivm', sep=',')
    conn.commit()
    print(f)

cur.execute(
    """
    ALTER TABLE 5.rivm
  ADD id  SERIAL PRIMARY KEY
    """
)
conn.commit()

ogr2ogr -f "PostgreSQL" PG:"host= dbname= user=5 password=__5___ port=" roads.json -nln roads –append

.\ogr2ogr  -f "PostgreSQL" PG:"host= dbname= user=5 password=__5___ port=" D:\study2019\courseware\Q2C2\assignment\roads\roads.json -nln roads append