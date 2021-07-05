import datetime
import time

# a = time.localtime()
# b = datetime.datetime.now()
#
# print(b)
# print(type(b))

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d"))
later = now+datetime.timedelta(days=30)
print(later.strftime("%Y-%m-%d"))





