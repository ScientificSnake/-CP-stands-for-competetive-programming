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

monthNames = ['January', 'February', 'March', 'April', 'May','June', 'July', 'August', 'September', 'October', 'November', 'December']
monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]

prefixmonths = []
prefixmonthsleap = []

total = 0
totalleap = 0
for i in range(12):
    prefixmonths.append(total)
    prefixmonthsleap.append(totalleap)
    total += monthdays[i]
    totalleap += monthdays[i]
    if i == 1:
        totalleap += 1 # leap year feb 29
# days before jan 1 monday 2024

# 365 days
# leap year is every 4 except 100s
ntests = int(input())
for _ in range(ntests):
    month, year = [int(x) for x in input().split()]

    if year < 2024:
        offsetdays = 0
        for year_i in range(year, 2024):
            offsetdays -= 1
            if year_is_leap(year_i):
                offsetdays -= 1
    if year > 2024:
        offsetdays = 0
        for year_i in range(2024, year):
            offsetdays += 1
            if year_is_leap(year_i):
                offsetdays += 1
    
    offsetdays %= 7
    if year_is_leap(year):
        offsetdays += prefixmonthsleap[month-1]
    else:
        offsetdays += prefixmonths[month-1]
    offsetdays %= 7
    offsetdays += 1 # 2024 started on a monday
    # first line
    print(f'      {monthNames[month-1]} {year}')
    print('Su Mo Tu We Th Fr Sa')
    calendarString = ""
    for _ in range(offsetdays):
        calendarString += '  '
    dayLetters = ['Su', 'Mo', 'Tu','We','Th','Fr','Sa']
    for newDay in range(1, monthdays[month]+1):
        daystr = " " + str(newDay)
        if len(daystr) == 2:
            daystr = " " + daystr

        calendarString += daystr
        if (newDay + offsetdays) % 7 == 0:
            calendarString += '\n'
    print(calendarString)




    