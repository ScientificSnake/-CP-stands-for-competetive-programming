# # of test cases
t = int(input())

# loop through each test case
for _ in range(t):
    length_of_array = int(input())
    strn = input().split(' ')

    n = [int(n) for n in strn]
    
    if n[0] == -1 and n[length_of_array - 1] == -1:
        diff_array_sum = 0
    if n[0] == -1:
        diff_array_sum = 0
        n[0] = n[length_of_array - 1]
    elif n[length_of_array - 1] == -1:
        diff_array_sum = 0
        n[length_of_array - 1] = n[0]
    else:
        diff_array_sum = n[length_of_array - 1] - n[0]

    print(abs(diff_array_sum))
    for i in n:
        if i == -1:
            i = 0
        print(str(i) + " ", end='')

    print()