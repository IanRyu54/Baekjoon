import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

number, weight = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(number)]
max_val = [0 for _ in range(weight + 1)]

things.sort()

for i in things:
    for j in range(weight, 0, -1):
        if(i[0] > j):
            break
        if(i[0] <= j):
            max_val[j] = max(i[1] + max_val[j - i[0]], max_val[j])
            
print(max_val[weight])