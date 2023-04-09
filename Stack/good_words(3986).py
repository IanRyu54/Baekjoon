import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
words = [input().split("\n")[0] for _ in range(num)]
result = 0

for i in words:
    temp = []
    good = 0
    for j in i:
        if(temp):
            if(temp[-1] == j):
                temp.pop()
                good += 1
            else:
                temp.append(j)
        else:
            temp.append(j)
        
    if(good == len(i) // 2 + len(i) % 2):
        result += 1

print(result)