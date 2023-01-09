#setwd()
airbox<-read.csv("submit/airbox/csv/combined_csv.csv",header=T)
head(airbox)
par(mfrow=c(1,2))
attach(airbox)
hist(PM10,nclass = 50,main="PM10_airbox")
hist(PM25,nclass = 50,main="PM25_airbox")
# hist(Airbox_NO2_1)
# boxplot(PM10,main="PM10_airbox")
# boxplot(PM25,main="PM10_airbox")
# plot(date,PM10, xlab="DATE", ylab="PM10",
#       main="pm10_airbox")
# plot(date,PM25, xlab="DATE", ylab="PM25",
#      main="pm25_airbox")

# detach(airbox)

sense<-read.csv("opensense/PM10.csv",header=T)
head(sense)
par(mfrow=c(1,2))
attach(sense)
hist(value,nclass = 50,main ="PM10_opensense")
#boxplot(value,main="PM10_opensense")
#hist(Airbox_NO2_1)
#plot(createdAt,value, xlab="DATE", ylab="PM10",
#     main="pm10_opensense")
detach(sense)
sense_pm25<-read.csv("opensense/PM25.csv",header=T)
attach(sense_pm25)
#boxplot(value,main="PM25_opensense")
hist(value,nclass = 50,main="PM25_opensense")
#plot(createdAt,value, xlab="DATE", ylab="PM25",
#     main="pm25_opensense")
detach(sense_pm25)

