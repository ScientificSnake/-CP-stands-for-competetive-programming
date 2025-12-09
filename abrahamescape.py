t = int(input())

for _ in range(t):
    a, b = [int(x) for x in input().split()]

    asqr = a ** 2

    if asqr - b == 1 or asqr - b < 0:
        print('no')
    else:
        print('yes')
        looptiles = asqr - b
        onefullloopline = False
        onepartial = 0
        rest = 0
        if looptiles >= a:
            onefullloopline = True
            rest = looptiles - a
        else:
            onepartial = looptiles
        
        # now print it
        if looptiles > 0:
            if onefullloopline:
                print('R' * (a-1) + 'L')
                for line in range(a-1):
                    if rest > 0 and rest <= a:
                        print('U' * rest + 'D' * (a-rest))
                        rest = 0
                    elif rest > 0 :
                        print(rest * 'U')
                        rest -= a
                    else:
                        print('D' * a)
            else:
                print('R' * (onepartial-1) + 'L' + "D" * (a - onepartial))
                for line in range(a-1):
                    print('D' * a)
        else:
            for i in range(a):
                print(a * 'U')

            