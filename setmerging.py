t = int(input())

for _ in range(t):
    s = input()
    setcount, n = [int(x) for x in s.split()]

    sets = []  # pair of [length, array]

    for i in range(setcount):
        s = input()
        setlength = int(s[0])

        thiset = [int(x) for x in s.split()[1:]]

        sets.append([setlength, thiset])