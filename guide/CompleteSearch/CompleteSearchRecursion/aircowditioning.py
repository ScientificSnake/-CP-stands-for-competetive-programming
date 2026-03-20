n_cows, m_aircons = [int(x) for x in input().split()]

cows = []
fans = []

for _ in range(n_cows):
    s, t, c = [int(x) for x in input().split()]
    cows.append((s,t,c))

for _ in range(m_aircons):
    a, b ,p, m = [int(x) for x in input().split()]
    fans.append((a,b,p,m))

min_price = float("inf")
stalls = []
for bmask in range(1 << m_aircons):
    stalls = [0] * 100
    this_cost = 0
    for i in range(m_aircons):
        if bmask & (1 << i):
            fanref = fans[i]
            # add the cooling and cost
            this_cost += fanref[3]
            for targeted_stalls in range(fanref[0], fanref[1] + 1):
                stalls[targeted_stalls] += fanref[2]
                
    # now we check if it was a valid thing
    fail = False
    for cow in cows:
        stall_area = stalls[cow[0]:cow[1]+1]
        if min(stall_area) < cow[2]:
            fail = True
            break
    if fail:
        continue
    min_price = min(min_price, this_cost)
print(min_price)
