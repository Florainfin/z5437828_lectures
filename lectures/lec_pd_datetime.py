""" lec_pd_datetime.py

Companion codes for the lecture on working with time-series data in Pandas
"""
import os
import datetime as dt
import pandas as pd
import toolkit_config as cfg


# Instance of `dt.datetime` with the current date/time
dt_now = dt.datetime.now()
# This will produce a string representing the date/time in `dt_now`
print(dt_now)
# This will confirm that `dt_now` is an instance of the `datetime` class
print(type(dt_now))  # --> <class 'datetime.datetime'>

s = 'Date in day/month/year format is: {}/{}/{} '.format(dt_now.day, dt_now.month, dt_now.year)
print(s)

# String representing the data included in the object
print(dt_now)
# This will give you a string representing how the instance could be constructed
print(repr(dt_now))

# Create another datetime instance with value 2021-08-21 13:24:27.283311
a_little_ago = dt.datetime(
    year=2021,
    month=8,
    day=21,
    hour=13,
    minute=27,
    second=1, microsecond=283311)
print(a_little_ago)

# Note that we don't have to pass all arguments
dt_other = dt.datetime(
    year=2021,
    month=8,
    day=21,
    )
print(dt_other)

# Let create two other datetime instances
dt0 = dt.datetime(year=2019, month=12, day=31)
dt1 = dt.datetime(year=2020, month=1, day=1)
# Operations between datetime objects will return timedelta objects
delta = dt1 - dt0
print(delta)
print(repr(delta))

# These two dates are 12 hours apart
t1 = dt.datetime(year=2020, month=12, day=31, hour=12)
t2 = dt.datetime(year=2020, month=12, day=31, hour=0)
new_delta = t1 - t2
print(new_delta)

start = dt.datetime(year=2020, month=12, day=31, hour=0)
delta = dt.timedelta(hours=12)
# This is the new date
end = start + delta
print(start)
print(end)

# Create a datatime object
date = dt.datetime(year=2020, month=12, day=31, hour=0)
# Create a string with the representation we want:
s = date.strftime('%Y-%m-%d')
print(s)

x = dt.datetime(year=2023, month=12, day=31, hour=9, minute=30, second=33)
y = x.strftime('%A of week number %U of the year %Y')
print(y)

CSVLOC = os.path.join(cfg.DATADIR, 'tsla_prc.csv')
prc = pd.read_csv(CSVLOC)


