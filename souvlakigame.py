t = int(input())

for _ in range(t):
    length = int(input())
    s = input()
    optimal = [int(x) for x in s.split()]
    optimal.sort()

    possible = True

    for index, element in enumerate(optimal):
        if index % 2 == 0:
            continue
        else:
            try:
                if element != optimal[index + 1]:
                    # this is the case where he can get griefed
                    possible = False
                    break
            except IndexError:
                pass
                # finishes the loop here anyways
    
    if possible:
        print('yes')
    else:
        print('no')