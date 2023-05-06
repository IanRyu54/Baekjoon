import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
dir = [[0, 1, 0], [1, 0, 0], [0, -1, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]]

floor_num, rows, columns = map(int, input().split())

while(floor_num and rows and columns):
    floor_info = []
    start_ind = []
    end_ind = []
    visited = [[[0 for _ in range(columns)] for _ in range(rows)] for _ in range(floor_num)]
    for i in range(floor_num):
        floor_info.append([])
        for j in range(rows):
            floor_info[i].append(input())
            if("S" in floor_info[i][j]):
                start_ind = [j, floor_info[i][j].index("S"), i]
            if("E" in floor_info[i][j]):
                end_ind = [j, floor_info[i][j].index("E"), i]
        input()

    now_ind = deque([start_ind])
    visited[start_ind[2]][start_ind[0]][start_ind[1]] = 1
    time_takes = 0
    arrived = 0
    while(not arrived and now_ind):
        for i in range(len(now_ind)):
            cur_ind = now_ind[0]
            if(cur_ind[0] == end_ind[0] and cur_ind[1] == end_ind[1] and cur_ind[2] == end_ind[2]):
                arrived = 1
                time_takes -= 1
                now_ind = []
                break
            now_ind.popleft()
            for j in dir:
                new_x = cur_ind[0] + j[0]
                new_y = cur_ind[1] + j[1]
                new_z = cur_ind[2] + j[2]
                if(new_x >= 0  and new_y >= 0 and new_z >= 0 and new_x < rows and new_y < columns and new_z < floor_num):
                    if(not visited[new_z][new_x][new_y] and floor_info[new_z][new_x][new_y] != "#"):
                        visited[new_z][new_x][new_y] = 1
                        now_ind.append([new_x, new_y, new_z])
        time_takes += 1
    
    if(arrived):
        print("Escaped in " + str(time_takes) + " minute(s).")
    else:
        print("Trapped!")
    floor_num, rows, columns = map(int, input().split())