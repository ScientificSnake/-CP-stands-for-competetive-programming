n_cows, m_aircons = [int(x) for x in input().split()]

cows = []
fans = []

for _ in range(n_cows):
    s, t, c = [int(x) for x in input().split()]
    cows.append((s,t,c))

for _ in range(m_aircons):
    a, b ,p, m = [int(x) for x in input().split()]
    fans.append((a,b,p,m))

for bmask in range(1 << m_aircons):
    for i in range(m_aircons):
        if bmask & (1 << m_aircons):
            fan = fans[i]
             