# 3.	Write a program to take two date and time values from the user and find the difference between two dates and time.

from datetime import datetime

# datetime in string format
str_dt1 = '2021/10/20 09:15:32.36980'
str_dt2 = '2022/2/20 04:25:42.120450'

# convert string to datetime
dt1 = datetime.strptime(str_dt1, "%Y/%m/%d %H:%M:%S.%f")
dt2 = datetime.strptime(str_dt2, "%Y/%m/%d %H:%M:%S.%f")

# difference between datetime in timedelta
delta = dt2 - dt1
print(f'Difference is {delta.days} days')
