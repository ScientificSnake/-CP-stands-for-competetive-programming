t = int(input())

for _ in range(t):
    # start on left and work backwards
    river = input()
    
    if '*<' in river or '><' in river or '>*' in river or '**' in river:
        time = -1
    else:
        # find the longest sequence >>>>> or <<<<<< or sometimes <<<<<*
        for options in ['*<', '*>']:
            if options == '*<':
                curlen1 = 0
                targetIndex = 0
                while True:
                    try:
                        if river[targetIndex] in options and targetIndex >= 0:
                            curlen1 += 1
                            targetIndex += 1
                        else:
                            break
                    except IndexError:
                        break
            elif options == '*>':
                curlen2 = 0
                targetIndex = len(river) - 1
                while True:
                    try:
                        if river[targetIndex] in options and targetIndex >= 0:
                            curlen2 += 1
                            targetIndex -= 1
                        else:
                            break
                    except IndexError:
                        break
        time = max(curlen1, curlen2)
    print(time)




        