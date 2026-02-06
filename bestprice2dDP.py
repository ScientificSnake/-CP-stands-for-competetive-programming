n, q = [int(x) for x in input().split()]
prices = [int(x) for x in input().split()]

best_prices = []
# count t, up to deal k [k][t]

highest_query = max(prices)

runnning_min = int("inf")
for price in prices:
    runnning_min = min(runnning_min, price)
    row_t = [None] * (highest_query + 1) # + 1 makes it 0 indexed
    row_t[0] = 0 # buying nothing never costs anything
    row_t[1] = runnning_min

# now we modify the top row (up to k = 0)
best_prices[0] = [i * prices[0] for i in range(highest_query)]

def bestPrice(target, k):
    if target <= 0:
        return 0
    if best_prices[k][target] != None:
        return best_prices[k][target]
    # two choices, use deal K or not

    choiceDontUseK = bestPrice(target, k -1)
    choiceUseK = bestPrice(target - pow(2, k)) + prices[k]
    result =  min(choiceUseK, choiceDontUseK)
    best_prices[k][target] = result
    
    
