# only 20 max apples

Napples = int(input())

appleWeights = [int(x) for x in input().split()]

def recurseiveWeightsMin(i : int , sum1 : int, sum2 : int):
    if i == (Napples):
        return abs(sum1 - sum2)
    
    return min(
        recurseiveWeightsMin(i +1, sum1 + appleWeights[i], sum2),
        recurseiveWeightsMin(i +1, sum1, sum2 + appleWeights[i])
    )

print(recurseiveWeightsMin(0, 0, 0))
