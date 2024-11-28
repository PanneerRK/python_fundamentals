#current date and time
import datetime

x = datetime.datetime.now()
print(x)

#print current year
print(x.year)
#print current Day name
print(x.strftime("%A"))