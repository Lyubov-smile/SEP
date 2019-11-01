from datetime import datetime, timedelta
#print(datetime.strftime(datetime.now() + timedelta(1), '%Y-%m-%d'))
d1 = datetime.strftime(datetime.now(), '%Y-%m-%d')
print(d1)

d3 = datetime.strftime(datetime.now() + timedelta(1), '%Y-%m-%d')
print(d3)

