from sys import stdin

def solve():
    tests = []
    ntests = int(next(stdin))
    maxn = 0
    for _ in range(ntests):
        a,b = [int(x) for x in next(stdin).split()]
        tests.append((a,b))
        maxn = max(a,maxn,b)

    sieveList = [0] * maxn

    for i in range(2, maxn+1):
        if sieveList[i] == 0:
            for j in range(i, maxn, i):
                sieveList[j] += 1

    # usaco.guide best preix sums

    prefixsums = [0]

    runningsum = 0
    for i, val in enumerate(sieveList):
        if val in [0,1]:
            # prime or power of prime
            runningsum -= 1
        else:
            if val % 2 == 0:
                runningsum += 1
            else:
                runningsum -= 1
        prefixsums.append(runningsum)
    

    for a,b in tests:
        print(prefixsums[b] -  prefixsums[a])


solve()