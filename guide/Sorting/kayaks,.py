npeople = int(input())

weights = [int(x) for x in input().split()]
weights.sort()

min_weight = float('inf')

for i in range(2*npeople):
    for j in range(i + 1, 2*npeople):
        instablity_sum = 0
        # j will always be larger than i 
        stashj = weights.pop(j)
        stashi = weights.pop(i)

        for kayak in range(0, (2*npeople) - 2, 2):
            w1 = weights[kayak+1]
            w2 = weights[kayak]
            instablity_sum += abs( w1-  w2)
        min_weight = min(instablity_sum, min_weight)
        weights.insert(i, stashi)   
        weights.insert(j, stashj)
print(min_weight)