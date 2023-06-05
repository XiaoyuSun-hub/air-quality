
NO237.df<-read.csv("submit\\ex3\\join37.csv",header=T)
NO239.df<-read.csv("submit\\ex3\\join39.csv",header=T)


NO2_37.df.new<-na.omit(NO237.df) 
NO2_39.df.new<-na.omit(NO239.df)

bias_h39=NO2_39.df.new$no2 - NO2_39.df.new$no2_rivm
bias_h37=NO2_37.df.new$no2 - NO2_37.df.new$no2_rivm


plot(NO2_39.df.new$date1,bias_h39,xlab="date", ylab="bias",
     main="hourly bias 39")

plot(NO2_37.df.new$date1,bias_h37,xlab="date", ylab="bias",
     main="hourly bias 37")

#boxplot(bias_h39, main="hourly bias 39")
#boxplot(bias_h37, main="hourly bias 37")


NO237.df<-read.csv("submit\\ex3\\joindaily37.csv",header=T)
NO239.df<-read.csv("submit\\ex3\\joindaily39.csv",header=T)


NO2_37.df.new<-na.omit(NO237.df) 
NO2_39.df.new<-na.omit(NO239.df)


bias_d39=NO2_39.df.new$no2 - NO2_39.df.new$no2_rivm
bias_d37=NO2_37.df.new$no2 - NO2_37.df.new$no2_rivm
#hist(bias_d39,nclass=30)

plot(NO2_39.df.new$date,bias_d39,xlab="date", ylab="bias",
 main="dayly bias 39")
plot(NO2_37.df.new$date,bias_d37,xlab="date", ylab="bias",
     main="dayly bias 37")





