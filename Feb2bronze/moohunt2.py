# ms are 0 os are 1
def getRelevantMasks(m, otups, n):
    boards = set()
    
    fixed_indices = {m, otups[0], otups[1]}
    floating_indices = [i for i in range(n) if i not in fixed_indices]
    
    base_mask = (1 << otups[0]) | (1 << otups[1])
    num_missing = n - 3
    for i in range(1 << num_missing):
        current_board = base_mask
        for bit_pos, original_idx in enumerate(floating_indices):
            if (i >> bit_pos) & 1:
                current_board |= (1 << original_idx)
        
        boards.add(current_board)
    return boards

n, k = [int(x) for x in input().split()]

masks = set()
moves = {}
for _ in range(k):
    # -1 for 0 indexing
    move = [int(x)-1 for x in input().split()]
    os = [move[1], move[2]]
    os.sort() # no diff between [4,5] [5,4]
    masks.update(getRelevantMasks(move[0], os, n))

    try:
        moves[(move[0], tuple(os))] += 1
    except:
        moves[(move[0], tuple(os))] = 1

maskscores = {}

for mask in masks:
    maskscore = 0
    for move, count in moves.items():
        m_bit = (1 << move[0])
        o_mask = (1 << move[1][0]) | (1 << move[1][1])
        if not (mask & m_bit) and (mask & o_mask) == o_mask:
            maskscore += count
    try:
        maskscores[maskscore] += 1
    except:
        maskscores[maskscore] = 1

highestscore = max(maskscores.keys())

possibles = maskscores[highestscore]

print(f"{highestscore} {possibles}")
        