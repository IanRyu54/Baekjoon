import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

nums, goal = map(int, input().split())

coins = [int(input()) for _ in range(nums)]
max_num = [-1 for _ in range(goal + 1)]

coins.sort()

result = 100000

max_num[0] = 0

for i in range(goal + 1):
    for j in coins:
        temp_res = 0

        if(j <= i and max_num[i - j] != -1):
            temp_res += max_num[i - j]
            temp_res += 1

            if(max_num[i] == -1):
                max_num[i] = temp_res
            else:
                if(temp_res < max_num[i]):
                    max_num[i] = temp_res

result = max_num[goal]

print(result)