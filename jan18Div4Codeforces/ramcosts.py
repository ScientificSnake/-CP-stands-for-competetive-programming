t = int(input())

for _ in range(t):
    n, m, h = [int(x) for x in input().split()]

    a = [int(x) for x in input().split()]

    net = {}

    

    for i in range(m):
        bi, ci = [int(x) for x in input().split()]
        bi -= 1
        try:
            net[bi] += ci
        except:
            net[bi] = ci
        if net[bi] + a[bi] > h:
            net.clear()

    o = []
    for i in range(n):
        try:
            o.append(a[i] + net[i])
        except:
            o.append(a[i])
        
    output = " ".join([str(c) for c in o])
    print(output)
    