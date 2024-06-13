import time
import calendar
print(time.time())
print(time.asctime(time.localtime(time.time())))
print()
attrList=["Year","Month","Day","Hour","Minutes","Seconds","Day of the week","Day of the year","Day Light Savings"]

for index,val in enumerate(time.localtime(time.time())):
    print(f"{attrList[index]}:{val}")

print(calendar.month(1999,5))
