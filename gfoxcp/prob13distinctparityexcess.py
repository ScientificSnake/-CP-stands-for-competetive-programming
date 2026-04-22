from math import ceil

from sys import stdin
from collections import deque
from functools import lru_cache


@lru_cache(256)
def factorsingle(num: int) -> tuple[tuple[int, int], bool]:
    cap = ceil(pow(num, 0.5))

    # start at 2 because we dont want to divide by 1
    divisors = range(2, cap + 1)

    for divisor in divisors:
        if divisor == num:
            continue
        quotient = num / divisor

        if quotient.is_integer():
            finalnew = (int(quotient), divisor)
            return finalnew, True
    return (-1, -1), False


fufcache = {}
fufcache : dict[int, frozenset]


def fullUniqueFactors(num: int):
    if num in fufcache:
        return fufcache[num]
    else:
        factors = set()
        facq = deque([num])

        while facq:
            tfactor = facq.popleft() 
            
            if tfactor in fufcache:
                factors.update(fufcache[tfactor])
                continue
            else:
                newnums, success = factorsingle(tfactor)

                if not success:
                    factors.add(tfactor) # it is prim
                else:
                    facq.extend(newnums)
        res = frozenset(factors)
        fufcache[num] = res
        return res    
    
@lru_cache
def isEvenprimefactors(n: int):
    factors = fullUniqueFactors(n)
    uniques = len(factors)

    if uniques % 2 == 0:
        return True
    else:
        return False


nlines = int(input())

for _ in range(nlines):
    a, b = [int(x) for x in input().split()]
    nums = range(a, b+1)

    evenparitycount = 0
    oddparitycount = 0
    
    for num in nums:
        if isEvenprimefactors(num):
            evenparitycount += 1
        else:
            oddparitycount += 1
    
    print(evenparitycount-oddparitycount)
