n, q = [int(x) for x in input().split()]
prices = [int(x) for x in input().split()]

best_prices = []
# count t, up to deal k [k][t]

querys = []

for _ in range(q):
    querys.append(int(input()))

highest_query = max(querys)

runnning_min = float("inf")
for price in prices:
    runnning_min = min(runnning_min, price)
    row_t = [None] * (highest_query + 1) # + 1 makes it 0 indexed
    row_t[0] = 0 # buying nothing never costs anything
    row_t[1] = runnning_min
    best_prices.append(row_t)

# now we modify the top row (up to k = 0)
best_prices[0] = [i * prices[0] for i in range(highest_query + 1)]

def bestPrice(target, k):
    if target <= 0:
        return 0
    if best_prices[k][target] != None:
        return best_prices[k][target]
    # two choices, use deal K or not

    choiceDontUseK = bestPrice(target, k -1)
    choiceUseK = bestPrice(target - pow(2, k), k) + prices[k]
    result =  min(choiceUseK, choiceDontUseK)
    best_prices[k][target] = result
    return result
    
# now actually do the things

for query in querys:
    print(bestPrice(query, n -1 ))  # -1 for 0 index shift
