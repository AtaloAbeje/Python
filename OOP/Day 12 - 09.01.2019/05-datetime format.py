
# Getting more control over formatting
# %a abbreviated day of the week: Mon, Tues, Wed
# %A full name of the day of week: Monday, Tuesday, Wednesday
# %d day of month: number 10 for 10th of January
# %b abbreviated month name: Jan, Feb, Mar
# %B full month name: January
# %m month as number: 01 for Jan
# %H hours
# %M minutes
# %S seconds
# %p AM or PM
# %y two number year
# %Y four number year

from datetime import datetime

now = datetime.now()

print(now.strftime("%a %A %d"))                 # --> Wed Wednesday 09

print(now.strftime("%b %B %m"))                 # --> Jan January 01

print(now.strftime("%A %B %d"))                 # --> Wednesday January 09

print(now.strftime("%H : %M : %S %p"))          # --> 13 : 54 : 23 PM

print(now.strftime("%y %Y"))                    # --> 19 2019