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


def index2d1d(x,y, width):
    return (y*width) + x

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
    visited = [False] * tmap.mapx * tmap.mapy
    visited : list[bool]

    visited[index2d1d(tmap.start[0], tmap.start[1], tmap.mapx)] = True

    mainq.append((tmap.start, 0))

    while True:
        try: 
            (x,y), time = pq.popleft()
        except:
            try:
                (x,y), time = mainq.popleft()
            except:
                break # nothing left

        totaldistremaining = abs(tmap.end[0]-x) + abs(tmap.end[1]-y)

        # pruning
        try:
            if time >= tmap.maxtime:
                continue
            if totaldistremaining + time >= tmap.maxtime:
                continue
        except AttributeError:
            pass  # does nto have max time

        adjs = getAdjCoordsBounded((x,y),tmap)
        adjs = [(x,y) for x,y in adjs if (tmap.map2d[y][x] != '#') and not visited[index2d1d(x, y, tmap.mapx)]]

        for nx, ny in adjs:
            if isTileLava(nx, ny, time +1, lavamap):
                continue
            else:
                if tmap.map2d[ny][nx] == 'E':
                    return True
                else:
                    visited[index2d1d(nx,ny, tmap.mapx)] = True

                    newtotaldistremaining = abs(tmap.end[0]-nx) + abs(tmap.end[1]-ny)
                    if newtotaldistremaining < totaldistremaining:
                        pq.append(((nx,ny),time+1)) # going in the right direction
                    else:
                        mainq.append(((nx,ny), time+1))
    return False


def getlavamap(tmap : mainmap):
    lava2d = [[float('inf')] * tmap.mapx for _ in range(tmap.mapy)]

    lavaQ = tmap.lava_q
    visited = [False] * tmap.mapx * tmap.mapy 
    for x,y in lavaQ:
        lava2d[y][x] = 0
        visited[index2d1d(x,y, tmap.mapx)] = True

    while len(lavaQ):
        x, y = lavaQ.popleft()
        if tmap.map2d[y][x] == 'E':
            tmap.noteEndCoveringTime(lava2d[y][x])
            # here you can break out because nothing should get past this time
            break
        adjs = getAdjCoordsBounded((x,y), tmap)
        adjs = [(nx,ny) for nx,ny in adjs if (tmap.map2d[ny]    [nx] not in ['#', 'L']) and not visited[index2d1d(nx, ny, tmap.mapx)]]
        # do not override previous lave or go on bedrock

        for nx, ny in adjs:
            visited[index2d1d(nx, ny, tmap.mapx)] = True
            lava2d[ny][nx] = lava2d[y][x] +1
            lavaQ.append([nx,ny])

    return lava2d


def getmap(inputdata):
    stime = time.time()
    map2d = []
    mapx, mapy = [int(x) for x in next(inputdata).split()]
    lavaset = Queue()
    start = (0,0)
    end = (0,0)

    startfound = False
    endfound = False

    for y in range(mapy):
        s = next(inputdata).strip()
        map2d.append(s)

        if not startfound:
            try: 
                start = (s.index('S'), y)
                startfound = True
            except:
                pass
        
        if not endfound:
            try:
                end = (s.index('E'), y)
                endfound = True
            except:
                pass

        if 'L' in s:
            [lavaset.append((x,y)) for x, char in enumerate(s) if char == 'L']
    
    result = mainmap(mapx, mapy, map2d, lavaset, start, end)
    endtime = time.time()
    print(f'Map state took {endtime-stime}')
    return result

def solve(inputdata):
    mapdata = getmap(inputdata)
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
    rawinputdata = stdin.readlines()
    inputdata = iter(rawinputdata)
    ntests = int(next(inputdata))

    for _ in range(ntests):
        solve(inputdata)


main()