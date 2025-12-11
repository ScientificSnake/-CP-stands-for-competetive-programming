from math import gcd

t = int(input())

# primes = set(2, 3, 5, 7, 11, 13, 17, 19)

for _ in range(t):
    arraylen = int(input())
    numlist = [int(x) for x in input().split()]

    numlist.sort()

    dehone = -1

    gcds = set()
    
    found = False

    for num in numlist:
        for i in range(2, 200000000):
            thisgcd = gcd(num, i)
            if thisgcd == 1:
                gcds.add(i)
                break
    print(min(gcds))
    