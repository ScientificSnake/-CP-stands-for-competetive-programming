t = int(input())

for _ in range(t):
    s = input()
    a, b = [int(x) for x in s.split()]

    abits = a.bit_length()

    maxa = (1 << (abits)) - 1

    if b > maxa:
        print('-1')
    elif a == b:
        print('0')
    else:
        print('2')
        # it can always be done in onestep
        print((a ^ b) ^ a)
        print(a)