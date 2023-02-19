import sys

nums = int(input())
max_num = -sys.maxsize
sum_all = 0

for i in range(nums):
    new_num = int(input())
    sum_all += new_num

    if max_num < new_num:
        max_num = new_num

sum_others = sum_all - max_num

final_difference = abs(max_num - sum_others)

if sum_others == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {final_difference}")
