nlines = int(input())

for _ in range(nlines):
    peaks = 0
    mrange = input()
    
    for index, char in enumerate(mrange):
        if index == 0:
            continue
        if index == (len(mrange) - 1):
            continue

        a = int(mrange[index-1])
        b = int(char)
        c = int(mrange[index+1])

        if b > a and b > c:
            peaks += 1
    print(peaks)
