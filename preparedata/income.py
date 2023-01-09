import psycopg2
from os import listdir,getcwd
from os.path import isfile, join
'''
__5___

 
The port at which the server
listens to requests is port 
'''
conn = psycopg2.connect(host="", dbname="", port="", user="",password="")
cur = conn.cursor()

cur.execute(
    """
    Drop table 5.income
    """
)
conn.commit()

#create table
cur.execute("""
CREATE TABLE 5.income
(
    municipality  text,
    disposable double precision
)
""")
conn.commit()
#batch copy csv files into the database
#path= getcwd()
mypath ="D:\study2019\courseware\Q3C2\geohealth\index\disposable_income_by_municipality_res_core_20162.csv"
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
with open(mypath, 'r') as f:
#     conn.commit()
    next(f)
    cur.copy_from(f, 'income', sep=',')
#     conn.commit()
# for f in onlyfiles:
#     with open(join(mypath, f), 'r') as f:
#     #Notice that we don't need the `csv` module.
#      next(f) # Skip the header row.
#      cur.copy_from(f, 'rivm', sep=',')
#     conn.commit()
#     print(f)
# #create and set primary key
# cur.execute(
#     """
#     ALTER TABLE 5.rivm
#   ADD id  SERIAL PRIMARY KEY
#     """
# )
conn.commit()
