import sys

def main():
    lines = sys.stdin.readlines()
    
    for line in lines:
        operations = 0

        while True:
            i = 0
            k = len(line) - 1 -i
            if line[i] == line[k]:
                i += 1
                continue
            



main()