def year_is_leap(year:int):
    if year % 4 == 0:
        if year %  100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

ntests = int(input())

month = [31,28,31,30,31,30,31,31,30,31,30,31]

prefixmonths = []
prefixmonthsleap = []

total = 0
totalleap = 0
for i in range(12):
    prefixmonths.append(total)
    prefixmonthsleap.append(totalleap)
    total += month[i]
    totalleap += month[i]
    if i == 1:
        totalleap += 1 # leap year feb 29
# days before jan 1 monday 2024

# 365 days
# leap year is every 4 except 100s
for _ in range(ntests):
    month, year = [int(x) for x in input().split()]

    if year < 2024:
        extradays = 0
        for year in range(year, 2024):
            extradays += 1
            if year_is_leap(year):
                extradays += 1
    if year