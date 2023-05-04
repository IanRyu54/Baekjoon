import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

row, column = map(int, input().split())
mazes = [input() for _ in range(row)]
visited = [[0 for _ in range(column)] for _ in range(row)]

index = deque([[0, 0]])
length = 0
found = 0

while(not found):
    for i in range(len(index)):
        curr_ind = index[0]
        index.popleft()
        for j in dir:
            new_x = curr_ind[0] + j[0]
            new_y = curr_ind[1] + j[1]
            if(new_x == column - 1 and new_y == row - 1):
                found = 1
                break
            if(new_x >=0 and new_y >= 0 and new_x < column and new_y < row):
                if(not visited[new_y][new_x] and mazes[new_y][new_x] == "1"):
                    visited[new_y][new_x] = 1
                    index.append([new_x, new_y])
    length += 1

print(length + 1)