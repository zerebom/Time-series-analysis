import datetime as time
import calendar


start_date=[]
end_date=[]

def Date(start_year,end_year):
    for year in range(start_year,end_year): 
        for month in range(1,13):
            start_date.append(str(time.date(year,month,1)))
            last_day = calendar.monthrange(year, month)[1]
            end_date.append(str(time.date(year,month,last_day)))
    return(start_date,end_date)        
        