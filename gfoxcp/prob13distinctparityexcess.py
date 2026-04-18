import math
from functools import lru_cache

@lru_cache
def factorsingle(nums: tuple):
    nums = tuple(set(nums))
    for num in nums:
        cap = math.ceil(math.sqrt(num))

        # start at 2 because we dont want to divide by 1
        divisors = range(2, cap + 1)

        for divisor in divisors:
            if divisor == num:
                continue
            quotient = num / divisor

            if quotient.is_integer():
                finalnew = [int(quotient), divisor]
                newnums = list(nums)
                newnums.remove(num)
                newnums.extend(finalnew)
                nums = tuple(newnums)
                return nums, True
    return nums, False


@lru_cache
def isEvenprimefactors(n: int):
    factors = (n,)
    while True:
        factors, notdone = factorsingle(factors)
        if not notdone:
            break
    factors = set(factors)
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
