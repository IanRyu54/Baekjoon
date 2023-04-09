import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

def cabbage():
    comp = 0
    for i in range(len(visited)):
        if(not visited[i]):
            dfs_cab(i)
            comp += 1
    return comp

def dfs_cab(loc):
    visited[loc] = 1
    for i in range(len(cab_loc)):
        x_diff = abs(cab_loc[i][0] - cab_loc[loc][0])
        y_diff = abs(cab_loc[i][1] - cab_loc[loc][1])
        if(not visited[i] and (x_diff + y_diff == 1)):
            dfs_cab(i)

test_num = int(input())

for i in range(test_num):
    width, height, num_cab = map(int, input().split())
    cab_loc = [list(map(int, input().split())) for _ in range(num_cab)]
    visited = [0 for _ in range(num_cab)]

    result = cabbage()
    
    print(result)