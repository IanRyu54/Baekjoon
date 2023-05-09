import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

case_num = int(input())
for _ in range(case_num):
    width, height = map(int, input().split())
    building_map = []
    start_ind = deque([])
    fire_ind = deque([])
    fired = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        temp = input()
        for j in range(len(temp)):
            if(temp[j] == "@"):
                start_ind.append([i, j])
                break
            elif(temp[j] == "*"):
                fire_ind.append([i, j])
                fired[i][j] = 1
        building_map.append(temp)

    escaped = 0
    time_takes = 0
    visited = [[0 for _ in range(width)] for _ in range(height)]
    visited[start_ind[0][0]][start_ind[0][1]] = 1
    while(start_ind and not escaped):
        for i in range(len(fire_ind)):
            cur_ind = fire_ind[0]
            fire_ind.popleft()
            for j in dir:
                new_x = cur_ind[0] + j[0]
                new_y = cur_ind[1] + j[1]
                if(new_x >= 0 and new_y >= 0 and new_x < height and new_y < width):
                    if(building_map[new_x][new_y] != "#" and not fired[new_x][new_y]):
                        fired[new_x][new_y] = 1
                        fire_ind.append([new_x, new_y])

        for i in range(len(start_ind)):
            cur_ind = start_ind[0]
            start_ind.popleft()
            for j in dir:
                new_x = cur_ind[0] + j[0]
                new_y = cur_ind[1] + j[1]
                if(new_x >= 0 and new_y >= 0 and new_x < height and new_y < width):
                    if(building_map[new_x][new_y] == "." and not visited[new_x][new_y] and not fired[new_x][new_y]):
                        visited[new_x][new_y] = 1
                        start_ind.append([new_x, new_y])
                else:
                    escaped = 1
                    
        time_takes += 1

    if(escaped):
        print(time_takes)
    else:
        print("IMPOSSIBLE")