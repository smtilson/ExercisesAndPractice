from datetime import date
from datetime import datetime

x = datetime.today()
y = date.today()
print(x)
print(type(x))
print(y)
print(type(y))
print(y.month, y.day, y.year)
xmas = date(year= 2021, month= 12, day=25)
print(xmas - y)