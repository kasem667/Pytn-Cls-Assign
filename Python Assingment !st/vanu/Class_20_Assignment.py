import datetime as dt

current_date = dt.date.today()

day = current_date.day
month = current_date.month

if day == 29 and month == 9:
    print("Happy Birthday.")
else:
    print("Today is not my birthday.")


import datetime as dt
import time
current_date_with_time = dt.datetime.today()
print(current_date_with_time)

current_date = dt.date.today()
print(current_date)

current_time = time.time()
print(current_time)

print(current_date.day)
print(current_date.month)
print(current_date.year)