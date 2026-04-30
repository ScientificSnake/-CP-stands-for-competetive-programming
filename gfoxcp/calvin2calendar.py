import calendar

def solve():
    ntests = int(input())
    calendar.setfirstweekday(calendar.SUNDAY)

    for _ in range(ntests):
        month, year = [int(x) for x in input().split()]
        s = calendar.month(year, month).lstrip()
        
        lines = s.split('\n')
        lines.pop()
        for i, line in enumerate(lines):
            if i >= 2:
                line = line.ljust(21)
            elif i ==0:
                line = ' ' *6 + line
            
            print(line)
            

        # print(' '*6, end='')
        # print(s.rstrip())
        print('-' * 20)

solve()
