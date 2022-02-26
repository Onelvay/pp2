import datetime

inp=datetime.datetime(2004, 1, 28)
now=datetime.datetime.now()
delta=now-inp
print(delta.total_seconds())
