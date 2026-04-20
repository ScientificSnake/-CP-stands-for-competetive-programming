from collections import deque as Queue
from sys import stdin
import time


class mainmap(): 
    def __init__(self, maxx, maxy, map2dlist, lavaset, start, end) -> None:
        self.mapx = maxx
        self.mapy = maxy
        self.map2d = map2dlist; self.map2d : list[list[str]]
        self.lava_q = lavaset; self.lavaset : Queue
        self.start = start
        self.end = end
    
    def noteEndCoveringTime(self, time):
        self.maxtime = time


def getAdjCoordsBounded(_pos : tuple[int,int], tmap : mainmap) -> list[tuple[int,int]]:
    x, y = _pos
    results = []

    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= nx < tmap.mapx and 0 <= ny < tmap.mapy:
            results.append((nx, ny)) 
    return results


def isTileLava(x, y, time, lavamap) -> bool:
    return lavamap[y][x] <= time

def bfsfindpath(tmap: mainmap, lavamap : list[list[float]]):
    mainq = Queue()
    pq = Queue()
    visited = set([tmap.start])

    mainq.append((tmap.start, 0))

    while True:
        try: 
            (x,y), time = pq.popleft()
        except:
            try:
                (x,y), time = mainq.popleft()
            except:
                break # nothing left

        totaldistremaining = abs(tmap.start[0]-x) + abs(tmap.start[1]-y)

        # pruning
        try:
            if time >= tmap.maxtime:
                continue
            if totaldistremaining + time >= tmap.maxtime:
                continue
        except AttributeError:
            pass  # does nto have max time

        adjs = getAdjCoordsBounded((x,y),tmap)
        adjs = [(x,y) for x,y in adjs if (tmap.map2d[y][x] != '#') and (x,y) not in visited]

        for nx, ny in adjs:
            if isTileLava(nx, ny, time +1, lavamap):
                continue
            else:
                if tmap.map2d[ny][nx] == 'e':
                    return True
                else:
                    visited.add((nx,ny))

                    newtotaldistremaining = abs(tmap.start[0]-nx) + abs(tmap.start[1]-ny)
                    if newtotaldistremaining < totaldistremaining:
                        pq.append(((nx,ny),time+1)) # going in the right direction
                    else:
                        mainq.append(((nx,ny), time+1))
    return False


def getlavamap(tmap : mainmap):
    lava2d = [[float('inf')] * tmap.mapx for _ in range(tmap.mapy)]

    lavaQ = tmap.lava_q

    for x,y in lavaQ:
        lava2d[y][x] = 0


    visited = set(tmap.lava_q)
    while len(lavaQ):
        x, y = lavaQ.popleft()
        if tmap.map2d[y][x] == 'e':
            tmap.noteEndCoveringTime(lava2d[y][x])
            # here you can break out because nothing should get past this time
            break
        adjs = getAdjCoordsBounded((x,y), tmap)
        adjs = [(nx,ny) for nx,ny in adjs if (tmap.map2d[ny][nx] not in ['#', 'l']) and (nx,ny) not in visited]
        # do not override previous lave or go on bedrock

        for nx, ny in adjs:
            visited.add((nx,ny))
            lava2d[ny][nx] = lava2d[y][x] +1
            lavaQ.append([nx,ny])

    return lava2d


def getmap():
    map2d = []
    mapx, mapy = [int(x) for x in stdin.readline().strip().split()]
    stime = time.time()
    lavaset = Queue()
    start = (0,0)
    end = (0,0)

    startfound = False
    endfound = False

    for y in range(mapy):
        s = stdin.readline().strip().lower()
        map2d.append(s)

        if not startfound:
            try: 
                start = (s.index('s'), y)
            except:
                pass
        
        if not endfound:
            try:
                start = (s.index('e'), y)
            except:
                pass

        if 'l' in s:
            [lavaset.append((x,y)) for x, char in enumerate(s) if char == 'l']
    
    result = mainmap(mapx, mapy, map2d, lavaset, start, end)
    endtime = time.time()
    print(f'Map state took {endtime-stime}')
    return result

def solve():
    
    mapdata = getmap()

    stime = time.time()
    lavamap = getlavamap(mapdata)
    endtime = time.time()
    print(f'Lava state took {endtime-stime}')

    stime = time.time()
    res = bfsfindpath(mapdata, lavamap)
    endtime = time.time()
    print(f'Movement state took {endtime-stime}')

    if res:
        print('Comin in hot!')
    else:
        print("I'm cooked")


def main():
    ntests = int(input())
    for _ in range(ntests):
        solve()


main()