t = int(input())

for _ in range(t):
    strlen = int(input())
    string = input()

    targetchar = string[-1]
    instancesoftargetchar = 0

    for char in string:
        if char == targetchar:
            instancesoftargetchar += 1
    
    ans = strlen - instancesoftargetchar

    # print(f'{ans} from {string}, target char was {targetchar}')
    print(ans)