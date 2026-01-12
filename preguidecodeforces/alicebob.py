t = int(input())

for _ in range(t):
    size_of_array, alice = [int(n) for n in input().split(' ')]

    array = [int(n) for n in input().split(' ')]

    larger = 0
    smaller = 0
    equal = 0

    for i in array:
        if alice < i:
            larger += 1
        elif alice > i:
            smaller += 1
        else:
            equal += 1

    if larger > smaller:
        bob = alice + 1
    if smaller > larger:
        bob = alice - 1
    else:
        bob = alice + 1
    print(bob)