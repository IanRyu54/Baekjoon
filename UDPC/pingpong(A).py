import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
winner = list(input().split("\n")[0] for _ in range(num))

dal = 0
pho = 0

for i in winner:
    if(i == "D"):
        dal += 1
    else:
        pho += 1
    
    if(max(dal - pho, pho - dal) > 1):
        break

print(str(dal) + ":" + str(pho))