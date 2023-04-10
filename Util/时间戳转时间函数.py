import time
import datetime
timestamp = 1681097778
utc_time = time.gmtime(timestamp)
print(utc_time)
iso_time = time.strftime("%Y-%m-%d %H:%M:%S", utc_time)

print(datetime.datetime.now())
print(iso_time)


a=[1,2,3,4,5,6,7]
print(a[1:])