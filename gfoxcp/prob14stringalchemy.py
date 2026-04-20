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

            # if they are different you can try get all 4 xx --- xx
            # and change all to something.




main()