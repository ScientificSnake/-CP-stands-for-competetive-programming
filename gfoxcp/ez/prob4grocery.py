ttests = int(input())
for _ in range(ttests):
    items_to_buy = input().split()
    m_stores = int(input())

    best_prices = {item : (None, float("inf")) for item in items_to_buy}

    best_at_stores = {}
    for _ in range(m_stores):
        storeName, itemcount = input().split()
        best_at_stores[storeName] = 0
        itemcount = int(itemcount)
        for _ in range(itemcount):
            item, price = input().split()
            price = float(price)
            if item in best_prices.keys():
                if price < best_prices[item][1]:
                    best_prices[item] = (storeName, price)

    for store, _ in best_prices.values():
        best_at_stores[store] += 1
    
    leader = None
    leaderBests = -float('inf')
    
    for store, bests in best_at_stores.items():
        if bests> leaderBests:
            leaderBests = bests
            leader = store
    
    print(f"{leader}'s prices are top G!!!")
