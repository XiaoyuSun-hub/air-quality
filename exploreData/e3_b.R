#setwd()
NO239.df<-read.csv("submit\\ex3\\join39.csv",header=T)
NO237.df<-read.csv("submit\\ex3\\join37.csv",header=T)

NO2_39.df.new<-na.omit(NO239.df)
NO2_37.df.new<-na.omit(NO237.df)


lm.1<-lm(no2_rivm~no2,data=NO2_39.df.new); summary(lm.1)
lm.2<-lm(no2_rivm~no2,data=NO2_37.df.new); summary(lm.2)


mlm.1<-lm(no2_rivm~no2 + temp + relhum,data=NO2_39.df.new); summary(mlm.1)

mlm.2<-lm(no2_rivm~no2 + temp + relhum,data=NO2_37.df.new); summary(mlm.2)


sqrtno2rivm37= sqrt(NO2_37.df.new$no2_rivm)
logno2rivm37=log1p(sqrtno2rivm37); 
no2_37= sqrt(NO2_37.df.new$no2)

sqrtno2rivm39= sqrt(NO2_39.df.new$no2_rivm)
logno2rivm39=log1p(sqrtno2rivm39); 
no2_39= sqrt(NO2_39.df.new$no2)

lm.37<-lm(logno2rivm37~no2_37); summary(lm.37)

lm.39<-lm(logno2rivm39~no2_39); summary(lm.39)

