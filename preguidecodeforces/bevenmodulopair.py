t = int(input())

for _ in range(t):
    arraylen = int(input())

    sequence = [int(i) for i in input().split()]

    overed_elems = set([])

    found = False

    for element in sequence:
        for prevmod in overed_elems:
            if (element % prevmod) % 2 == 0:
                found = True
                x = prevmod
                y = element
                break
        for elem in overed_elems:
            if (elem % element) == 0:
                overed_elems.remove(elem)
        if found:
            break
        overed_elems.add(element)

    if found:
        print(str(x) + " " + str(y))
    else:
        print("-1")