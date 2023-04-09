import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

lengths = int(input())

result = [1 for _ in range(10)]

result[0] = 0

for i in range(lengths - 1):
    temp = result[:]
    for j in range(len(result)):
        if(j == 0):
            result[j] = temp[j + 1]
        elif(j == 9):
            result[j] = temp[j - 1]
        else:
            result[j] = (temp[j - 1] + temp[j + 1]) % 1000000000


print(sum(result) % 1000000000)