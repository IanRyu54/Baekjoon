import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
orders = [list(input().split("\n")[0].split()) for _ in range(num)]

stacks = []

for i in orders:
    if(i[0] == "push"):
        stacks.append(i[1])
    elif(i[0] == "pop"):
        if(stacks):
            print(stacks.pop())
        else:
            print(-1)
    elif(i[0] == "size"):
        print(len(stacks))
    elif(i[0] == "empty"):
        if(stacks):
            print(0)
        else:
            print(1)
    else:
        if(stacks):
            print(stacks[-1])
        else:
            print(-1)