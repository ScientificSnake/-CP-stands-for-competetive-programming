import sys

sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")

ncows = int(input())

cowsDict = dict()

for _ in range(ncows):
    s, t, b = [int(x) for x in input().split()]

    cowsDict[s] = [t, b]

running_bucketUse = 0
peak_buckets = 0

in_use_buckets = {}

times = list(cowsDict.keys())
times.sort()

toRemove = []

for cowTime in times:
    toRemove.clear()
    for key, value in in_use_buckets.items():
        if key <= cowTime:
            running_bucketUse -= value
            toRemove.append(key)
    running_bucketUse += cowsDict[cowTime][1]

    for key in toRemove:
        in_use_buckets.pop(key)

    # add to running list
    in_use_buckets[cowsDict[cowTime][0]] = cowsDict[cowTime][1]

    if running_bucketUse > peak_buckets:
        peak_buckets = running_bucketUse
print(peak_buckets)


