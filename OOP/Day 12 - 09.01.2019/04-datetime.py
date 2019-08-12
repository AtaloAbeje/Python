# Datetime Module
from datetime import datetime

now = datetime.now()

print(now.date())           # --> 2019-01-09

print(now.year)             # --> 2019

print(now.month)            # --> 1

print(now.hour)             # --> 13

print(now.minute)           # --> 50

print(now.second)           # --> 17

print(now.time())           # --> 13:50:17.718526
