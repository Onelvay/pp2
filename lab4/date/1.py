import datetime
from time import strftime

d = datetime.timedelta(days=-5)
y=datetime.datetime.now()
n = y + d

print(n.strftime('%x'))
