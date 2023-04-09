import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
balloons = list(map(int, input().split()))
indexes = [i for i in range(1, num + 1)]
ind = 0

for i in range(num):
    temp = balloons.pop(ind)
    print(indexes.pop(ind), end = "")
    if(temp > 0):
        temp -= 1

    ind += temp
    ind %= max(len(balloons), 1)

    if(i != num - 1):
        print(" ", end = "")