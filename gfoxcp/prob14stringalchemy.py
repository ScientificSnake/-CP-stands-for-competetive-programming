import sys

def main():
    for rline in sys.stdin:
        line = rline.strip()
        operations = 0
        i = 0
        while True:
            k = len(line) - 1 -i

            if i >= k:
                break
            
            if i == k-1 and line[i] != line[k]:
                operations += 1
                break


            if line[i] == line[k]:
                i += 1
                continue
            else:
                if k-i > 2:
                    str1 = line[i] + line[i+1]
                    str2 = line[k] + line[k-1]
                    # str 2 is reversed cuz wonky
                    if (str1[0] != str2[0]) and (str1[1] != str2[1]):
                        operations += 1 
                        # you can do it in one with match
                        # from AB-----CD
                        # to   DC-----CD
                        i += 2
                        continue
                    else:
                        # you have something like
                        # AB----BC
                        # you have to change both to
                        # XX----XX
                        operations += 2
                        i += 2
                        continue
                else:
                    # if L-L then it would have been caught before
                    # so just change LxR to LyL
                    operations += 1
                    break
        print(operations)
main()