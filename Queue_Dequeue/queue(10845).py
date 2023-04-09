from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
orders = [input().split("\n")[0].split() for _ in range(num)]
queues = deque([])

for i in orders:
    if(i[0] == "push"):
        queues.append(i[1])
    else:
        if(queues):
            if(i[0] == "pop"):
                print(queues.popleft())
            elif(i[0] == "size"):
                print(len(queues))
            elif(i[0] == "empty"):
                print(0)
            elif(i[0] == "front"):
                print(queues[0])
            else:
                print(queues[-1])
        else:
            if(i[0] == "empty"):
                print(1)
            elif(i[0] == "size"):
                print(0)
            else:
                print(-1)