input_nums = [int(n) for n in input().split(' ')]
input_nums.sort()
first, second, third = input_nums
if (third - first) >= 10:
    print("check again")
else:
    print(f'final {second}')    