t = int(input())

for _ in range(t):
    roots = int(input())

    output = ""
    for i in range(roots):
        output += str(i+1) + " "
    output.rstrip()
    print(output)