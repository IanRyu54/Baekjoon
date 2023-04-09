import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
paren = [list(input().split("\n")[0]) for _ in range(num)]

for i in paren:
    y_n = 0
    for j in i:
        if(j == "("):
            y_n += 1
        else:
            y_n -= 1
        if(y_n < 0):
            break

    if(y_n == 0):
        print("YES")
    else:
        print("NO")