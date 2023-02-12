from datetime import datetime
x=datetime.now()
date_format='%d.%m.%Y. %X'
print(x.strftime(date_format))
