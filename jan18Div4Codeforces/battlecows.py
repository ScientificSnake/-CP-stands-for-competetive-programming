import math
t = int(input())

for _ in range(t):
    n, q = [int(x) for x in input().split()]

    ao = [[int(x)] for x in input().split()]
    lastcowpos = 0
    for _ in range(q):
        a = ao.copy()
        bi, ci = [int(x) for x in input().split()]

        bi -= 1

        a[bi][0] = ci


        lastcowpos = bi
        

        lastcowpositioninstack = 0

        for round in range(n):
            for cowstackindx in range(0, len(a), 2):

                stack1 = a[cowstackindx]
                stack2 = a[cowstackindx+1]

                stack1power = stack1[0]
                i = 0
                for cow in stack1:
                    if i == 0:
                        i += 1
                        continue
                    stack1power ^= cow
                    i += 1
                stack2power = stack2[0]
                i = 0
                for cow in stack2:
                    if i == 0:
                        i += 1
                        continue
                    stack2power ^= cow
                    i += 1
                
                if stack1power >= stack2power:
                    if cowstackindx == lastcowpos:
                        lastcowpositioninstack += len(stack2)
                    a[cowstackindx] = stack2 + stack1
                else:
                    if cowstackindx+ 1 == lastcowpos:
                        lastcowpositioninstack += len(stack1)
                    a[cowstackindx] = stack1 + stack2
            a = a[::2]
            lastcowpos = lastcowpos//2
        cowsabove = pow(2, n) - lastcowpositioninstack - 1
        print(cowsabove)