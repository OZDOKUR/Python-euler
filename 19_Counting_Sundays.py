import datetime

startDate = datetime.date(1901, 1, 1)
endDate = datetime.date(2000, 12, 31)

count = 0

while startDate <= endDate:
    if startDate.weekday() == 6:
        count += 1
    startDate += datetime.timedelta(days=1)

print("The number of months that fall on a Sunday =",count)
