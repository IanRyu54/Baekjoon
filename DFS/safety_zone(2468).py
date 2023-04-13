import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
def find_area(loc):
    visited[loc[1]][loc[0]] = 1
    for i in dir:
        new_x = loc[0] + i[0]
        new_y = loc[1] + i[1]
        if(new_x >= 0 and new_y >= 0 and new_x < num and new_y < num):
            if(not visited[new_y][new_x] and zones[new_y][new_x] > height):
                find_area([new_x, new_y])

num = int(input())
zones = [list(map(int, input().split())) for _ in range(num)]

max_height = 0
min_height = 100
for i in zones:
    max_height = max(max_height, max(i))
    min_height = min(min_height, min(i))

result = 0
for height in range(min_height - 1, max_height):
    visited = [[0 for _ in range(num)] for _ in range(num)]
    num_area = 0
    for i in range(num):
        for j in range(num):
            if(not visited[i][j] and zones[i][j] > height):
                find_area([j, i])
                num_area += 1
                
    result = max(result, num_area)

print(result)