from datetime import datetime 

# => Get current date and time 
getdatetime = datetime.now()
print("Current data and time = ",getdatetime) # Current data and time =  2025-01-26 22:21:06.096382
print("Year = ",getdatetime.year) # 2025
print("Month = ",getdatetime.month) # 1
print("Day = ",getdatetime.day) # 1
print("Hour = ",getdatetime.hour) # 1
print("Minute = ",getdatetime.minute) # 1
print("Second = ",getdatetime.second) # 1

# => Create a specific datetime
setdatetime = datetime(2000,5,25,13,30,45)
print("My Birthday = ",setdatetime) #  2000-05-25 13:30:45

# => strftime , String Formating Date time
getnow = datetime.now()
formatdatetime = getnow.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date Time =",formatdatetime)

# => strptime(), Convert a string to datetime
strdate = "2025-January-26 22:30:50"
converteddate = datetime.strptime(strdate,"%Y-%B-%d %H:%M:%S")
print("Converted datetime = ",converteddate)

# https://docs.python.org/3/library/datetime.html 