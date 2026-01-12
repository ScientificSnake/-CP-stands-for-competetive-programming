t = int(input())

for _ in range(t):
    arraylen = int(input())

    sequence = input().split()

    odds = 0
    evens = 0

    isPure = True

    for elem in sequence:
        if int(elem) % 2 == 0:
            evens += 1
            if odds >= 1 and evens >= 1:
                isPure = False
                break
        else:
            odds += 1
            if odds >= 1 and evens >= 1:
                isPure = False
                break
    intseq = [int(x) for x in sequence]
    
    if isPure:
        print(' '.join([str(x) for x in intseq]))
    else:
        intseq.sort()
        print(' '.join([str(x) for x in intseq]))