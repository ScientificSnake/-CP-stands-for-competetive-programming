import sys
sys.stdin = open("backforth.in", "r")
sys.stdout = open("backforth.out", "w")

init_barn1_buckets = [int(x) for x in input().split()]
init_barn2_buckets = [int(x) for x in input().split()]

solutions = set()

def recursively_move_milk(i : int, t1:int, t2:int, b1:list, b2:list):
    if i == 4:
        solutions.add(t1)
        return
    elif i % 2 == 0:
        # first to second (tuesday and thursday)
        for bucket in b1:
            newb1 = b1.copy()
            newb1.remove(bucket)
            newb2 = b2.copy()
            newb2.append(bucket)
            recursively_move_milk(i+1, t1 - bucket, t2 + bucket, newb1, newb2)
    else:
        # second to first (wednesday and friday)
        for bucket in b2:
            newb2 = b2.copy()
            newb2.remove(bucket)
            newb1 = b1.copy()
            newb1.append(bucket)
            recursively_move_milk(i+1, t1 + bucket, t2 - bucket, newb1, newb2)

recursively_move_milk(0, 1000, 1000, init_barn1_buckets, init_barn2_buckets)

print(len(solutions))