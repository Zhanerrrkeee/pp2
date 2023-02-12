from datetime import datetime

import math 
date_one=datetime(1999,2,1)
date_two=datetime(1999,2,2)
difference=abs(date_one - date_two)
seconds=difference.total_seconds()
print(seconds)
