t, k = [int(x) for x in input().split()]

def flip(char, flips):
    flips = flips % 2
    if flips == 1:
        if char == 'O':
            return 'M'
        else:
            return "O"
    else:
        return char


for _ in range(t):
    n = int(input())
    s = input()

    print("YES")

    if (k == 1):
        flips = 0
        entered = []

        for char in reversed(s):
            enteredchar = flip(char, flips)

            if enteredchar == 'O':
                flips += 1
            entered.append(enteredchar)
        print("".join(reversed(entered)))
