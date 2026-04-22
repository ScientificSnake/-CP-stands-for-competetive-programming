lines = int(input())

vowstr = input()

for _ in range(lines-1):
    vowstr += ("\n" + input())

name = input()

while True:
    front, sep, back = vowstr.partition("BLANK")
    if front == vowstr:
        break
    else:
        vowstr = front + name + back

print(vowstr)

