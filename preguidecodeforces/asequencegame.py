t = int(input())

for _ in range(t):
    arraysize = int(input())

    elements = [int(x) for x in input().split(' ')]
    target = int(input())

    elements.sort()

    if target >= elements[0] and target <= elements[-1]:
        print('yes')
    else:
        print('no')