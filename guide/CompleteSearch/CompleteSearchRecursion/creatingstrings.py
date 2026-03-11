string = input()

chars = list(string)

strings = []

def recurse(left: list, string):
    options = len(left)
    if options == 0:
        strings.append(string)
        return
    for i in range(options):
        newleft = left[:i]
        newleft.extend(left[i+1:])
        recurse(newleft, string + left[i])
recurse(chars, '')

strings = list(set(strings))
strings.sort()
print(len(strings))
[print(i) for i in strings]