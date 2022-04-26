import datetime
from time import strftime
import pytz

# dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)

# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

print(dt_mtn.strftime('%B %d, %Y'))
dt_str = 'July 26, 2016'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to string
# strptime - String to datetime
# mtn_tz = pytz.timezone("US/Mountain")

# dt_mtn = mtn_tz.localize(dt_mtn)
# dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)

# dt_today = datetime.datetime.date()
# dt_now = datetime.datetime.now()

# t = datetime.datetime()

# print(t)

# today = datetime.date.today()
# print(today.year)

# tdelta = datetime.timedelta(days=7)

# print(today - tdelta)

# date2 = date1 + timedelta
# timedelta = datel + date2

# bday = datetime.date(2022, 12, 21)

# till_bday = bday - today

# print(till_bday.total_seconds())