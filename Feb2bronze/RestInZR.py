n, q = [int(x) for x in input().split()]

deals = [int(x) for x in input().split()]

memoizedBestDeals = {}

def getBestDeal(needed: int):
    try:
        return memoizedBestDeals[needed]
    except:
        rates = [(min(needed, pow(2, i))/cost) for i, cost in enumerate(deals)]
        bestRate = max(rates)
        dealnum = rates.index(bestRate)

        # buy as much as posible without going over
        mult = needed // pow(2, dealnum)

        mult = max(1, mult)

        result = [pow(2,dealnum) * mult, deals[dealnum] * mult]
        memoizedBestDeals[needed] = result
        return result
toPrint = []
for _ in range(q):
    countPurchased = 0
    needed = int(input())
    spent = 0
    while 0 < needed:
        count, cost = getBestDeal(needed)
        countPurchased += count
        spent += cost
        needed -= count
    toPrint.append(spent)

[print(spent) for spent in toPrint]