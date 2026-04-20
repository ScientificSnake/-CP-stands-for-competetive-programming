# lava can engulf the end block
from queue import Queue
coordtype = tuple[int,int]

def getAdjacents(_pos: tuple, _map: dict, mapx, mapy) -> list[tuple[coordtype, str]]:
    x, y = _pos
    results = []
    for adj in [(x+1,y), (x-1,y), (x,y+1),(x,y-1)]:
        try:
            results.append((adj, _map[adj]))
        except KeyError:
            if adj[0] < 0 or adj[1] < 0:
                continue
            if adj[0] > (mapx-1) or adj[1] > (mapy-1):
                continue
                # if gets through both its empty

            results.append((adj, '.'))

            # case 1 its out of bounds 2 case two its empty
    
    results = [i for i in results if i[1] != '#']
    return results


def getAdjacentsRaw(_pos, mapx, mapy) -> list[tuple[int,int]]:
    x, y = _pos
    results = [(x+1,y), (x-1,y), (x,y+1),(x,y-1)]

    results = [i for i in results if i[0] >= 0 and i[1] >= 0]
    results = [i for i in results if i[0] <= (mapx-1) and i[1] <= (mapy-1)]
    return results


def solve():
    mapx, mapy = [int(x) for x in input().split()]
    map = []
    start = (0,0)
    end = (0,0)

    lavas = set()

    for y in range(mapy):
        s = input()
        map.append(s.lower())
        for x, char in enumerate(s):
            if char == 'S':
                start = (x,y)
            elif char == 'E':
                end = (x,y)
            elif char == "L":
                lavas.add((x,y))
    
    farthestLavaTimeCalculated = 0
    
    lavareachstime = [[-1 for _ in range(mapx)] for _ in range(mapy)]

    for x,y in lavas:
        lavareachstime[y][x] = 0

    lavastopsprogressingbool = False
    lastlavaprogression = -1


    def isTileLava(time:int, x, y):
        nonlocal lavastopsprogressingbool, farthestLavaTimeCalculated
        if time <= farthestLavaTimeCalculated:
            lavatime = lavareachstime[y][x]
            if lavatime == -1:
                return False
            else:
                if time <= lavatime:
                    return True
                else:
                    return False
        else:
            if lavastopsprogressingbool:
                lavatime = lavareachstime[y][x]
                if lavatime == -1:
                    return False
                else:
                    return True
            else:
                while time > farthestLavaTimeCalculated:
                    progressmade = False
                    for x, y in lavas:
                        adjs = getAdjacentsRaw((x,y), mapx, mapy)

                        for newx, newy in adjs:
                            if lavareachstime[newy][newx] == -1:
                                progressmade = True
                                lavareachstime[newy][newx] = time
                    
                    if not progressmade:
                        lavastopsprogressingbool = True
                        break
                lavatime = lavareachstime[y][x]
                if lavatime == -1:
                    return False
                else:
                    return True



    bfsQ = Queue()
    bfsQ.put((start[0], start[1], 0))
    possible = False
    visited = set()
    while not bfsQ.empty():
        x, y, time = bfsQ.get()
        

        if isTileLava(time, x, y):
            continue
        try:
            if lavamap[pos] == 'l':
                continue
            elif lavamap[pos] == 'e':
                possible = True
                break
        except KeyError:
            pass
        visited.add(pos)
        adjacents = getAdjacents(pos, lavamap, mapx, mapy)
        adjacents = [i for i in adjacents if i[0] not in visited]
        adjacents = [i for i in adjacents if i[1] != 'l']

        for adj in adjacents:
            bfsQ.put((adj[0],time+1))
        

    if possible:
        print('Comin in hot!')
    else:
        print("I'm cooked")
    del lavamaps



ntests = int(input())
for _ in range(ntests):
    solve()