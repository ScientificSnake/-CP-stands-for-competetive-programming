nlines = int(input())

fuel = {
    "Stick" : 1,
    "Coal" : 8,
    "Lava Bucket" : 100,
    "CharCoal" : 12
}
total = 0
for _ in range(nlines):
    s = input()
    total += fuel[s]
print(total)
