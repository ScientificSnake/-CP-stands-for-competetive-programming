import itertools
import math
NCows = int(input())

class Cow:
    cowIdCounter = 0

    def __init__(self, dir, x, y) -> None:
        self.dir = dir
        self.x = x
        self.y = y
        self.collisions = []
        self.hasStopped = False
        self.id = Cow.cowIdCounter
        Cow.cowIdCounter += 1

class Collision:
    def __init__(self, x, y, time) -> None:
        self.x = x
        self.y = y
        self.time = time

cows: list[Cow] = []

for _ in range(NCows):
    dir, x, y = input().split()
    cows.append(Cow(dir, int(x), int(y)))

for cow1, cow2 in itertools.pairwise(cows):
    if cow1.dir == cow1.dir:
        if cow1.dir == 'N':
            if cow1.x == cow2.x:
                collisiony = max(cow1.y, cow2.y)
                collisionx = cow1.x
        if cow1.dir == 'S':
            if cow1.x == cow2.x:
                collisionx = cow1.x
                collisiony = min(cow1.y, cow2.y)
        if cow1.dir == 'W':
            if cow1.y == cow2.y:
                collisionx = min(cow1.x, cow2.x)
                collisiony = cow2.y
        if cow1.dir == 'E':
            if cow1.y == cow2.y:
                collisionx = max(cow1.x, cow2.x)
                collisiony = cow2.y
    else:
        if (ord(cow1.dir) + ord(cow2.dir)) == (ord('N') + ord('S')):
            distance = math.ceil(abs(cow1.y - cow2.y))

            if cow1.y < cow2.y:
                collisiony = cow1.y + distance
                collisionx = cow1.x
            else:
                collisiony = cow1.y - distance
            
                collisiony = cow1 - distance
        elif (ord(cow1.dir) + ord(cow2.dir)) == (ord("W") + ord("E")):
            distance = math.ceil(abs(cow1.x - cow2.x))
