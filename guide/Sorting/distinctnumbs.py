import sys

def solve():
    # .read().split() captures all input and splits it by whitespace
    # This is much faster than calling input() in a loop or splitting once
    data = sys.stdin.read().split()

    # data[0] is 'n', we ignore it
    # data[1:] contains the actual numbers
    # Passing the slice directly to set() is very efficient
    unique_count = len(set(data[1:]))
    
    print(unique_count)

if __name__ == "__main__":
    solve()