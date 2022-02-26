import datetime
from time import strftime
from tkinter import Y


d_today1=datetime.datetime.now()
y=datetime.timedelta(days=1)
yes=d_today1-y
tom=d_today1+y
d_yes=(d_today1)+(datetime.timedelta(days=-1))
d_tom=(d_today1)+(datetime.timedelta(days=+1))

print(d_today1.strftime('%x'))
print(d_yes.strftime('%x'))
print(d_tom.strftime('%x'))


print(yes.strftime('%A'))
print(tom.strftime('%A'))
