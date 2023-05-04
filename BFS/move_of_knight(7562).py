import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
dir = [[1, 2], [2, 1], [-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, -2], [2, -1]]

case_nums = int(input())

for i in range(case_nums):
    length = int(input())
    now_ind = deque([list(map(int, input().split()))])
    to_ind = list(map(int, input().split()))
    visited = [[0 for _ in range(length)] for _ in range(length)]

    found = 0
    moving = 0
    while(not found):
        for i in range(len(now_ind)):
            curr_ind = now_ind[0]
            if(curr_ind[0] == to_ind[0] and curr_ind[1] == to_ind[1]):
                found = 1
                moving -= 1
                break
            now_ind.popleft()

            for j in dir:
                new_x = curr_ind[0] + j[0]
                new_y = curr_ind[1] + j[1]
                if(new_x >= 0 and new_y >= 0 and new_x < length and new_y < length):
                    if(not visited[new_y][new_x]):
                        visited[new_y][new_x] = 1
                        now_ind.append([new_x, new_y])
        moving += 1

    print(moving)