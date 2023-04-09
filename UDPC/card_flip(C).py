import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
nums = [0 for _ in range(num)]
k = 0

print("YES")
for i in range(num - 1, 0, -1):
    if(k % 2 == 0):
        nums[num - (k // 2) - 1] = i
    else:
        nums[k // 2] = i
    k += 1

nums[k // 2] = num

for i in range(num):
    print(nums[i], end = "")
    if(i != num - 1):
        print(" ", end = "")
    else:
        print()

k = 0
for i in range(num):
    if(k % 2 == 0):
        print(num - (k // 2), end = "")
    else:
        print(k // 2 + 1, end = "")

    if(i != num - 1):
        print(" ", end = "")
    k += 1