# Read number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):
    n = int(input())
    
    if not (n % 2 == 0):
        answer = 0
    else:
        answer = n //4 + 1
    # Your solution here
    
    print(answer)