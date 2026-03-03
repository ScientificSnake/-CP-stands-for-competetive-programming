import sys

sys.stdout = open("tracing.out", "w")
sys.stdin = open("tracing.in", "r")


n, t = [int(x) for x in input().split()]
infectedMain = [int(i) for i in input().strip()]
shakes = []

for _ in range(t):
    shakes.append([int(x) for x in input().split()])

shakes.sort()

def simulate(cowZero):
    maxk = -float("inf")
    mink = float("inf")
    for k in range(251):
        shakeTimes = [0] * n
        infected = [0] * n
        infected[cowZero] = 1
        for i in range(len(shakes)):
            cow1, cow2 = shakes[i][1], shakes[i][2]

            cow1wasinfected = False
            cow2wasinfected = False
            if infected[cow1-1]:
                cow1wasinfected = True
            if infected[cow2-1]:
                cow2wasinfected = True

            if infected[cow1-1] and shakeTimes[cow1-1] < k:
                infected[cow2-1] = 1
            elif infected[cow2-1] and shakeTimes[cow2 - 1] < k:
                infected[cow1-1] = 1
            
            if cow1wasinfected:
                shakeTimes[cow1-1] += 1
            if cow2wasinfected:
                shakeTimes[cow2-1] += 1
            
            

        if (infected == infectedMain):
            maxk = max(maxk, k)
            mink = min(mink, k)
    return (mink, maxk)

ans_maxk = -float("inf")
ans_mink = float('inf')
possiblezeros = 0
for i in range(len(infectedMain)):
    if infectedMain[i]:
        result = simulate(i)
        if result[0] != float("inf"):
            ans_mink = min(ans_mink, result[0])
            ans_maxk = max(ans_maxk, result[1])
            possiblezeros += 1
    
if ans_maxk == 250:
	ans_maxk = "Infinity"

print(possiblezeros, ans_mink, ans_maxk)
        



    
