from datetime import datetime,timedelta

date_format='%d.%m.%Y'

x=datetime.now()

yesterday=x - timedelta(days=1)

today=x

tomorrow=x + timedelta(days=1)

print( yesterday.strftime(date_format))
print(today.strftime(date_format))
print(tomorrow.strftime(date_format))
