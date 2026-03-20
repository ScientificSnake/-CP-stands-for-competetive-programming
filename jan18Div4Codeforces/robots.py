t = int(input())

for _ in range(t):
    n, m, k = [int(x) for x in input().split()]

    robots = [int(x) for x in input().split()]
    spikes = {int(x) for x in input().split()}

    instruction_string = input()
    for char in instruction_string:
        move = -1 if char == 'L' else 1
        
        for i in range(len(robots)-1, -1, -1):
            robots[i] += move
            if robots[i] in spikes:
                robots.pop(i)
        print(len(robots))
