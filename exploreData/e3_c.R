set.seed(123) # To same results when the simulation is repeated
NO239.df<-read.csv("submit\\ex3\\join39.csv",header=T)
NO237.df<-read.csv("submit\\ex3\\join37.csv",header=T)
 # we use the r function runif() to generate uniform distribution
NO2_39.df.new<-na.omit(NO239.df)
NO2_37.df.new<-na.omit(NO237.df)  


mlm.39<-lm(no2_rivm~no2 + temp + relhum,data=NO2_39.df.new); summary(mlm.39)
mlm.37<-lm(no2_rivm~no2 + temp + relhum,data=NO2_37.df.new); summary(mlm.37)


 # Airbox_NO2_2 values
NO2_39<-NO2_39.df.new$no2
NO2_37<-NO2_39.df.new$no2
temp_39<-NO2_39.df.new$temp
temp_37<-NO2_39.df.new$temp
relhum_39<-NO2_39.df.new$relhum
relhum_37<-NO2_39.df.new$relhum
  
newdata39<-data.frame(no2=runif(n=10, min=min(NO2_39),max=max(NO2_39)),
                      temp=runif(n=10, min=min(temp_39),max=max(temp_39)),
                      relhum=runif(n=10, min=min(relhum_39),max=max(relhum_39)));
                      newdata39
newdata37<-data.frame(no2=runif(n=10, min=min(NO2_37),max=max(NO2_37)),
                      temp=runif(n=10, min=min(temp_37),max=max(temp_37)),
                      relhum=runif(n=10, min=min(relhum_37),max=max(relhum_37)));
newdata37
y_pred39<-predict.lm(mlm.39,newdata = newdata39, interval="prediction", level= 0.95); y_pred39
y_est39<-predict.lm(mlm.39,newdata = newdata39, interval="confidence", level=0.95); y_est39

# y_pred37<-predict.lm(mlm.37,newdata = newdata37, interval="prediction", level= 0.95); y_pred37
# y_est37<-predict.lm(mlm.37,newdata = newdata37, interval="confidence", level=0.95); y_est37


