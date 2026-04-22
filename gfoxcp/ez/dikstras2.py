import queue

def getAdjacents(_pos: tuple, _map: dict) -> list[tuple[tuple, str]]:
    x, y = _pos
    results = []
    for adj in [(x+1,y), (x-1,y), (x,y+1),(x,y-1)]:
        try:
            results.append((adj, _map[adj]))
        except KeyError:
            pass
    return results

def keepOrNotStandAlone():
    """retrieves input by its self"""
    map = {}
    map : dict[tuple[int,int], str]
    distances = {}
    strin = input()
    strin = strin.replace(':',' ')
    strin = strin.replace('x',' ')
    stats = strin.split()
    bombs, mapwidth, mapheight = [int(x) for x in stats]
    visited = set()
    unvisited = set()
    for y in range(mapheight):
        s = input()
        for x, char in enumerate(s):
            char = char.lower()
            map[(x,y)] = char
            if char == 's':
                start = (x,y)
                distances[(x,y)] = 0
                visited.add((x,y))
            else:
                distances[(x,y)] = float('inf')
                unvisited.add((x,y))
    
    q = queue.Queue()
    pos = start
    q.put(pos)
    while not q.empty():
        pos = q.get()
        curdist = distances[pos]
        adjacents = [x for x in getAdjacents(pos, map) if x[0] in unvisited]
        for newpos, tileval in adjacents:
            if tileval == 'r':
                distances[newpos] = min(distances[newpos], curdist + 1)
            else:
                distances[newpos] = min(distances[newpos], curdist)
            
            if distances[newpos] <= bombs:
                visited.add(newpos)
                unvisited.remove(newpos)
                q.put(newpos)

                # wincon
                if tileval == 'e':
                    return True
    return False

ntests = int(input())

for _ in range(ntests):
    valid = keepOrNotStandAlone()
    if valid:
        print('Keep')
    else:
        print('Delete')
    


    
         
        