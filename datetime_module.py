from datetime import datetime
from datetime import date

d=datetime.now()
print(d.day,d.month,d.year)
print(d.hour,d.minute,d.second)

print(datetime.now())
print(datetime.today())
print(datetime.today())
print("Today date is (by date): ",date.today())


print("strftime display time: ",d.strftime("%H:%M:%S"))
print("stftime show date:",d.strftime("%Y %m %d --%B"))
print("Current month is:",d.strftime("-%B-"))
print("Current weekend day is:",d.strftime("%A"))





