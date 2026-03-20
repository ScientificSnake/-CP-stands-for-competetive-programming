t = int(input())

for _ in range(t):
    arraylen = int(input())

    array = [int(x) for x in input().split()]

    n = max(array)

    print(n * arraylen)