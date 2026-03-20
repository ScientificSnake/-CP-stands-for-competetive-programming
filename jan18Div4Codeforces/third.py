t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    maxStreak = 0
    currentStreak = 0
    last = 0
    for i, v in enumerate(a):
        if i == 0:
            last = v
            currentStreak = 1
            continue

        if v == (last + 1):
            currentStreak += 1
        elif v == last:
            pass
        else:
            maxStreak = max(maxStreak, currentStreak)
            currentStreak = 1
        last = v
    maxStreak = max(maxStreak, currentStreak)
    print(maxStreak)

        