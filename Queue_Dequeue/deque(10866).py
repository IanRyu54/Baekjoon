from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
orders = [input().split("\n")[0].split() for _ in range(num)]
temp = deque([])

for i in orders:
    order = i[0]
    if(order == "push_front"):
        temp.appendleft(i[1])
    elif(order == "push_back"):
        temp.append(i[1])
    elif(order == "size"):
        print(len(temp))
    elif(order == "empty"):
        if(len(temp)):
            print(0)
        else:
            print(1)
    else:
        if(temp):
            if(order == "pop_front"):
                print(temp.popleft())
            elif(order == "pop_back"):
                print(temp.pop())
            elif(order == "front"):
                print(temp[0])
            else:
                print(temp[-1])
        else:
            print(-1)