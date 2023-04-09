import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def cabbage():
    comp = 0
    for i in cab_coor:
        if(not visited[i[0]][i[1]]):
            dfs_cab(i)
            comp += 1
    return comp

def dfs_cab(loc):
    visited[loc[0]][loc[1]] = 1
    for i in direc:
        x = loc[0] + i[0]
        y = loc[1] + i[1]
        if(x < width and y < height and x >= 0 and y >= 0):
            if(not visited[x][y] and (cab_loc[x][y] == 1)):
                dfs_cab([x, y])

test_num = int(input())

for i in range(test_num):
    width, height, num_cab = map(int, input().split())
    cab_loc = [[0 for _ in range(height)] for _ in range(width)]
    cab_coor = [list(map(int, input().split())) for _ in range(num_cab)]

    for j in cab_coor:
        cab_loc[j[0]][j[1]] = 1

    visited = [[0 for _ in range(height)] for _ in range(width)]

    result = cabbage()
    
    print(result)