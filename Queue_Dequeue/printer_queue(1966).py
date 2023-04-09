from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
docs = [[list(map(int, input().split())), deque(list(map(int, input().split())))] for _ in range(num)]

for i in docs:
    result = 0
    goal = i[1][i[0][1]]
    max_doc = max(i[1])
    i[1][i[0][1]] = 0

    while(True):
        if(i[1][0] == 0):
            if(goal != max_doc):
                i[1].append(i[1].popleft())
            else:
                result += 1
                break
        else:
            if(max_doc != i[1][0]):
                i[1].append(i[1].popleft())
            else:
                i[1].popleft()
                max_doc = max(max(i[1]), goal)
                result += 1

    print(result)