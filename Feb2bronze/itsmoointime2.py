t, k = [int(x) for x in input().split()]

def flip(charcode, flips):
    flips = flips %2
    if flips == 1:
        return charcode ^ 1



for _ in range(t):
    n = int(input())
    s = input()

    print("YES")

    if (k==1):
        flips = 0
        enteredstr = 0

        for char in reversed(s):
            