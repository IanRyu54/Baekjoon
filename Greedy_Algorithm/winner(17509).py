import sys

sys.stdin = open('input.txt', 'r')

problems = [list(map(int,input().split())) for _ in range(11)]

problems = sorted(problems)
result = 0
temp = 0

for i in problems:
    temp = temp + i[0]
    result = result + temp
    result = result + i[1] * 20

print(result)