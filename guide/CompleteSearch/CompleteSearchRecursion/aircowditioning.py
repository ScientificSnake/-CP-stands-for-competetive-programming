n_cows, m_aircons = [int(x) for x in input().split()]

def ranges_overlap(r1, r2):
    # FIXME SHOULD BE FAN FULLY ENCLOSES COW NOT JUST AND PART
    return r2[0] <= r1[1] and r2[1] >= r1[0]

cows = []
fans = []

for _ in range(n_cows):
    s, t, c = [int(x) for x in input().split()]
    cows.append((s,t,c))

for _ in range(m_aircons):
    a, b ,p, m = [int(x) for x in input().split()]
    fans.append((a,b,p,m))

min_price = float("inf")
coolings = {}
for bmask in range(1 << m_aircons):
    coolings = {(cow[0], cow[1]) : 0 for cow in cows}
    this_cost = 0
    for i in range(m_aircons):
        if bmask & (1 << i):
            fanref = fans[i]
            # add the cooling and cost
            this_cost += fanref[3]
            for crange in coolings:
                if ranges_overlap(crange, (fanref[0], fanref[1])):
                    coolings[crange] += fanref[2]
    
    # now we check if it was a valid thing
    fail = False
    for index, (crange, coolingval) in enumerate(coolings.items()):
        if cows[index][2] > coolingval:
            fail = True
            break
    if fail:
        continue
    min_price = min(min_price, this_cost)
print(min_price)


             