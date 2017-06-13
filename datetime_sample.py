# -*- coding: utf-8 -*-

from datetime import datetime

now = datetime.now()
print(now.isoformat())

nextyear = datetime(2018, 1, 1)
delta = nextyear - now
print(delta)
print(delta.days)
