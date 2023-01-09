# epoch time
# http://data.aireas.com/api/v2/airboxes/history/10/1546297200/1548889200
# The maximum period of time returned by the API is 30 days, regardless of the passed in arguments.
# If you need to retrieve more than 30 days of data, do so by dividing the wanted period in smaller sized chunks.

import requests
import json
import datetime

# download station air observation data
url = 'http://data.aireas.com/api/v2/airboxes/history/{0}/{1}/{2}'
startTime= int(datetime.datetime(2019,1,1,0,0).timestamp())
print(type(startTime))
endTime= int(datetime.datetime(2019,1,31,0,0).timestamp())
# the number of stations is 39
for stationid in range(1,40):
    newUrl=url.format(stationid,startTime,endTime)
    print(newUrl)
    response = requests.request('GET', newUrl)
    jsonObj = json.loads(response.text) # convert text response into a dictionary
    with open("airbox/"+str(stationid)+'_'+str(startTime)+'_'+str(endTime)+'.json', 'w') as jsonfile:
        json.dump(jsonObj, jsonfile)

# download the road
# 152878.7543,378989.1854,166249.2103,389795.9651
# https://geodata.nationaalgeoregister.nl/nwbwegen/wfs?service=wfs&version=2.0.0&request=GetCapabilities
wfsUrl = 'https://geodata.nationaalgeoregister.nl/nwbwegen/wfs?service=wfs&version=2.0.0&request=GetFeature&outputFormat=application/json&typeNames=nwbwegen:wegvakken&srsName=urn:ogc:def:crs:EPSG::28992&bbox='
roadUrl = wfsUrl + '152878.7543,378989.1854,166249.2103,389795.9651'
response = requests.request('GET', roadUrl)
jsonObj = json.loads(response.text)  # convert text response into a dictionary
with open('roads.json', 'w') as jsonfile:
    json.dump(jsonObj, jsonfile)
print('roads download')
