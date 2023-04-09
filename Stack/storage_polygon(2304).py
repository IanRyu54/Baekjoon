import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
pillars = [list(map(int, input().split())) for _ in range(num)]
pillars.sort(key= lambda x : x[1], reverse= True)
temp = []
low_max = 0
high_max = 0
result = 0

for i in pillars:
    if(not low_max):
        result += i[1]
        low_max = i[0]
        high_max = low_max
    else:
        if(i[0] < low_max):
            diff = low_max - i[0]
            low_max -= diff
        elif(i[0] > high_max):
            diff = i[0] - high_max
            high_max += diff
        else:
            continue
            
        result += diff * i[1]

print(result)