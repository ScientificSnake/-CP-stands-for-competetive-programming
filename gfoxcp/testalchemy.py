import sys

def main():
    for rline in sys.stdin:
        line = rline.strip()
        if not line: continue
        
        operations = 0
        i = 0
        n = len(line)

        while i < n // 2:
            k = n - 1 - i
            if line[i] != line[k]:
                operations += 1
                i += 2
            else:
                i += 1
                
        print(operations)

main()