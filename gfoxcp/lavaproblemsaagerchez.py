import sys

def solve():
    # Read all input at once and use an iterator to grab values one by one
    input_data = sys.stdin.read().split()
    if not input_data: return
    it = iter(input_data)
   
    for _ in range(int(next(it))):
        R, C = int(next(it)), int(next(it))
        # the grid grows
        grid = [list(next(it)) for _ in range(R)]
       
        lava = []
        steve = []
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 'L': lava.append((r, c))
                if grid[r][c] == 'S': steve.append((r, c))

        success = False
        while steve and not success:
            # So the lava lavamaxes here
            next_lava = []
            for r, c in lava:
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] in '.SE':
                        grid[nr][nc] = 'L'
                        next_lava.append((nr, nc))
            lava = next_lava
           
            next_steve = []
            for r, c in steve:
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0 <= nc < C:
                        if grid[nr][nc] == 'E':
                            success = True; break
                        if grid[nr][nc] == '.':
                            grid[nr][nc] = 'V'
                            next_steve.append((nr, nc))
                if success: break
            steve = next_steve

        print("Comin in hot!" if success else "I'm cooked")

solve()
