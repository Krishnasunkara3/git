import datetime
print(dir(datetime))
#['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 
#'__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']



#date:
kri = datetime.date(1997,8,3)
print(kri)
print(kri.year)
print(kri.month)
print(kri.day)

#timedelta : used ofr adding and deleting days
t_delta = kri+datetime.timedelta(days = 365)
print(t_delta)

#DayName, MonthName Day-#, Year
print(kri.strftime("%A,%B %d,%Y"))
message = 'krishna was born on {:%A,%B %d,%Y}'
print(message.format(kri))

birth_date = datetime.date(1997,8,3)        #date class
birth_time = datetime.time(5,30,0)          #time class
birth_datetime = datetime.datetime(1997,8,3,5,30,0)     #datetime class
print(birth_date) 
       
print(birth_time)        #by using birthtime object we can access hours,minutes and seconds
print(birth_time.hour)
hour_delta = birth_time + datetime.timedelta(hours = 10)
print(hour_delta)       #timedelta for hours

print(birth_time.minute)
print(birth_time.second)

print(birth_datetime)       #by using datetime object we can access all the six parameters
print(birth_datetime.year)
print(birth_datetime.month)
print(birth_datetime.day)
print(birth_datetime.hour)
print(birth_datetime.minute)
print(birth_datetime.second)

#The default format of date time is YYYY/MM/DD HH:MM:SS:MS
#to view the present date and time
now = datetime.datetime.today()
print(now)    #it prints the present date and  time in addition it shows milliseconds also
print(now.microsecond)

#convert string to datetime

msg = '03/08/1998'
print(datetime.datetime.strptime(msg,'%d/%m/%Y'))