

import csv, json,os
from datetime import datetime

path=os.getcwd()
director = path+'\\airbox'
print(director)
os.chdir(director)
#for (dirpath, dirnames, filenames) in os.walk(director):
filenames = [f for f in os.listdir('.') if os.path.isfile(f)]
#for files in os.walk(path+'\\airbodata1'):
for file in filenames:
        inputFile= open(file)
        data = json.load(inputFile)  # load json content
        # this could be move to outside the for to create one
        #with open('output.csv', 'w', newline='\n', encoding='utf-8')
        outputFile = open("csv\\"+file.split('.')[0]+'.csv', 'w', newline='\n', encoding='utf-8') #load csv file
        inputFile.close()
        output = csv.writer(outputFile) #create a csv.write
        list_calibrated = list()
        list_calibrated.append('airbox_id')
        for key in data[0]['readings_calibrated']:
            if key != 'GPS':
                list_calibrated.append(key)
            else:
                list_calibrated.append('GPS_lat')
                list_calibrated.append('GPS_lon')
        list_calibrated.append('date')
        print(str(list_calibrated))
        output.writerow(list_calibrated)

        for row in data:
            list_values = list()
            list_values.append(data[0]['airbox_id'])
            for key in row['readings_calibrated']:
                if key != 'GPS':
                    list_values.append(row['readings_calibrated'][key])
                else:
                    list_values.append(row['readings_calibrated']['GPS']['lat'])
                    list_values.append(row['readings_calibrated']['GPS']['lon'])


            print(row['when']['measured']['$date'])
            print(type(row['when']['measured']['$date']))
            time=row['when']['measured']['$date']/1000
            dt_object = datetime.fromtimestamp(time)
            list_values.append(dt_object)
            print(str(list_values))
            output.writerow(list_values)


