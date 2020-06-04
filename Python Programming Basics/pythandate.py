import datetime 
import calendar 
  
def findDay(date): 
    born = datetime.datetime.strptime(date, '%Y %m %d').weekday()

    print(born)


    
    return (calendar.day_name[born]) 
  
# Driver program 
date = '1980 05 17'
print(findDay(date)) 