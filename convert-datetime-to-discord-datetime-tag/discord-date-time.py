import time
import calendar
from dateutil.tz import tzoffset
from datetime import timedelta

# validations
date_str = input("Enter time to convert in 'YYYY-MM-DD HH:MM:SS ±aa:bb' where aa:bb is the time zone offset from UTC")
must_be_decimals = {0:"Year",1:"Year",2:"Year",3:"Year",
                    5:"Month",6:"Month",
                    8:"Day",9:"Day",
                    11:"Hours",12:"Hours",
                    14:"Minutes",15:"Minutes",
                    17:"Seconds",18:"Seconds",
                    21:"Offset Hours",22:"Offset Hours",
                    24:"Offset Minutes",25:"Offset Minutes"}
for i in must_be_decimals.keys():
    try:
        int(date_str[i])
    except ValueError:
        print("%s should be in decimal digits" % must_be_decimals[i])
year = int(date_str[0:4])
month = int(date_str[5:7])
day = int(date_str[8:10])
hour = int(date_str[11:13])
minute = int(date_str[14:16])
seconds = int(date_str[17:19])
timezone = date_str[20:26]

offset_dir = timezone[0]
if(offset_dir!='+' or offset_dir!='-'):
    raise ValueError("UTC offset should begin with + or -")

tz_hours = int(timezone[1:3])
if(tz_hours > 12):
    raise ValueError("Offset hours cannot be more than 12")

tz_mins = int(timezone[4:6])
if(tz_mins >= 60 or tz_mins < 0):
    raise ValueError("Offset minutes must be from 0 to 59")

delta = timedelta(seconds = (tz_hours*3600+tz_mins*60) if offset_dir=="+" else (-1*tz_hours*3600+tz_mins*60))
timezone_offset = tzoffset("some_timezone", delta)

