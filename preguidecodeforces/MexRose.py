t = int(input())

for _ in range(t):
    s = input()
    _, target = s.split()
    target = int(target)
    s = input()
    a = s.split()

    number_of_targets = 0
    found_less_thans = (target) * [False]
    missinglowers = target

    for char in a:
        num = int(char)
        if num < target:
            if found_less_thans[num] is False:
                missinglowers -= 1
                found_less_thans[num] = True
        elif num == target:
            number_of_targets += 1

    print(max(missinglowers, number_of_targets))

    found_less_thans.clear()
