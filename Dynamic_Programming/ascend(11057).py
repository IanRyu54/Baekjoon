import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

lengths = int(input())
result = [1 for _ in range(10)]

for i in range(lengths - 1):
    temp = result[:]
    for j in range(len(result)):
        result[j] = sum(temp[0 : j + 1]) % 10007

print(sum(result) % 10007)