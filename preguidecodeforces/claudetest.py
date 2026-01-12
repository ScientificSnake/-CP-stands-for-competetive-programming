def solve(s):
    n = len(s)
    
    # Check for infinite sailing possibility with BFS considering choices at *
    def can_reach_cycle(start):
        from collections import deque
        queue = deque([(start, frozenset([start]))])
        
        while queue:
            pos, visited = queue.popleft()
            
            if s[pos] == '<':
                next_pos = pos - 1
                if 0 <= next_pos < n:
                    if next_pos in visited:
                        return True
                    queue.append((next_pos, visited | {next_pos}))
            elif s[pos] == '>':
                next_pos = pos + 1
                if 0 <= next_pos < n:
                    if next_pos in visited:
                        return True
                    queue.append((next_pos, visited | {next_pos}))
            else:  # '*'
                for next_pos in [pos - 1, pos + 1]:
                    if 0 <= next_pos < n:
                        if next_pos in visited:
                            return True
                        queue.append((next_pos, visited | {next_pos}))
        
        return False
    
    # Check if any starting position leads to infinite
    for start in range(n):
        if can_reach_cycle(start):
            return -1
    
    # Find maximum time with BFS
    def max_time_from(start):
        from collections import deque
        queue = deque([(start, 0)])
        max_t = 0
        
        visited_states = set()
        visited_states.add(start)
        
        while queue:
            pos, time = queue.popleft()
            
            if s[pos] == '<':
                next_pos = pos - 1
                if next_pos < 0:
                    max_t = max(max_t, time + 1)
                elif next_pos not in visited_states:
                    visited_states.add(next_pos)
                    queue.append((next_pos, time + 1))
            elif s[pos] == '>':
                next_pos = pos + 1
                if next_pos >= n:
                    max_t = max(max_t, time + 1)
                elif next_pos not in visited_states:
                    visited_states.add(next_pos)
                    queue.append((next_pos, time + 1))
            else:  # '*'
                for next_pos in [pos - 1, pos + 1]:
                    if next_pos < 0 or next_pos >= n:
                        max_t = max(max_t, time + 1)
                    elif next_pos not in visited_states:
                        visited_states.add(next_pos)
                        queue.append((next_pos, time + 1))
        
        return max_t
    
    result = 0
    for start in range(n):
        result = max(result, max_time_from(start))
    
    return result

t = int(input())
for _ in range(t):
    s = input().strip()
    print(solve(s))