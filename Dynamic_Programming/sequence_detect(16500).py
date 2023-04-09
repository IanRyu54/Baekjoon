import sys

input = sys.stdin.readline

ori_string = input().split('\n')[0]
numbers = int(input())
words = [input().split('\n')[0] for _ in range(numbers)]
res_list = [False for _ in range(len(ori_string) + 1)]

res_list[0] = True
for i in range(len(ori_string)):
    if not res_list[i]:
        continue

    for j in words:
        if ori_string[i : i + len(j)] == j:
            res_list[i + len(j)] = True

print(int(res_list[len(ori_string)]))