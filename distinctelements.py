t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    b = [int(x) for x in s.split()]

    a = []

    for i, bi in enumerate(b):
        if i == 0:
            a.append('1')
        else:
            x = bi - (i + 1) - b[i-1]
            
            if x == 0:
                a.append(str(i + 1))
            else:
                a.append(a[abs(x) - 1])

    print(' '.join(a))