import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

word = input().split("\n")[0]
uc = 0
dp = 0

for i in word:
    if(i == "U" or i == "C"):
        uc += 1
    else:
        dp += 1

k = 0

if(uc > dp // 2 + dp % 2):
    k = 1
    print("U", end = "")
if(dp > 0):
    k = 1
    print("D", end = "")
    print("P", end = "")
    
if(k == 0):
    print("C")