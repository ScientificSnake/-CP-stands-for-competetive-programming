import queue

possiblekeys = ['a', 'b', 'c', 'd']
possibledoors = ['A','B','C','D']

class scoutAreaResults():
    def __init__(self, doorsFound : list[tuple[tuple[int,int],str]], keysFound : list[str], endFound : bool) -> None:
        self.found_doors = doorsFound
        self.found_keys = keysFound
        self.end_found = endFound


def getAdjacents(_pos: tuple, _map: dict) -> list[tuple[tuple, str]]:
    x, y = _pos
    results = []
    for adj in [(x+1,y), (x-1,y), (x,y+1),(x,y-1)]:
        try:
            results.append((adj, _map[adj]))
        except KeyError:
            pass
    
    results = [i for i in results if i[1] != 'W']
    return results


def scoutArea(startpos :tuple[int,int], map: dict[tuple[int,int], str]) -> scoutAreaResults:
    q = queue.Queue()
    visited = set()
    visited : set[tuple[int,int]]

    foundDoors = []
    foundKeys = []

    visited.add(startpos)
    q.put(startpos)
    pos = startpos
    while not q.empty():
        pos = q.get()
        adjacents = [i for i in getAdjacents(pos, map) if i[0] not in visited]

        for newpos, tileval in adjacents:
            if tileval in possibledoors:
                foundDoors.append((newpos, tileval))
            elif tileval in possiblekeys:
                foundKeys.append(tileval)
            elif tileval == 'E':
                results = scoutAreaResults(foundDoors, foundKeys, True)
                return results
                    
            visited.add(newpos)
            if tileval not in possibledoors:
                q.put(newpos)
    
    results = scoutAreaResults(foundDoors, foundKeys, False)
    return results


def openDoors(keys: list[str], doors : list[tuple[tuple[int,int],str]], mape):
    keys = [i.upper() for i in keys]
    skeys = set(keys)
    progress = False
    doors_to_open = []
    for coord, door in doors:
        if door in skeys:
            progress = True
            doors_to_open.append(coord)

    for coord in doors_to_open:
        mape[coord] = '*'
    return progress

def solve():
    ntests = int(input())
    for _ in range(ntests):
        s = input()
        s = s.replace(' x ', ' ')
        width, height = [int(x) for x in s.split()]

        map = {}
        for y in range(height):
            line = input()
            for x, char in enumerate(line):
                map[(x,y)] = char
                if char == "S":
                    startpos = (x,y)
        
        while True:
            scout = scoutArea(startpos, map)

            if scout.end_found:
                print("accept")
                break
            
            progress = openDoors(scout.found_keys, scout.found_doors, map)

            if not progress:
                print("reject")
                break

if __name__ == '__main__':     
    solve()
            

