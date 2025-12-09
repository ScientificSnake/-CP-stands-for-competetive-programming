t = int(input())

running_list = []

for _ in range(t):

    listlen = int(input())

    a = input().split()

    uniques = set()

    for i in a:
        uniques.add(i)
    
    x = uniques

    print(len(uniques) *2 - 1)