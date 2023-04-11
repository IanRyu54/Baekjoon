import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
def calc_area(loc):
    global result
    visited[loc[1]][loc[0]] = 1
    result += 1
    for i in dir:
        new_x = loc[0] + i[0]
        new_y = loc[1] + i[1]
        if(new_x >= 0 and new_y >= 0 and new_x < width and new_y < height):
            if(not visited[new_y][new_x] and maps[new_y][new_x]):
                calc_area([new_x, new_y])

height, width, num_rectangle = map(int, input().split())
rectangles = [list(map(int, input().split())) for _ in range(num_rectangle)]
maps = [[1 for _ in range(width)] for _ in range(height)]
visited = [[0 for _ in range(width)] for _ in range(height)]

for i in rectangles:
    for j in range(i[0], i[2]):
        for k in range(i[1], i[3]):
            maps[k][j] = 0

result = 0
res_list = []
for i in range(height):
    for j in range(width):
        if(maps[i][j] and not visited[i][j]):
            calc_area([j, i])
            res_list.append(result)
        result = 0

res_list.sort()

print(len(res_list))

for i in range(len(res_list) - 1):
    print(res_list[i], end = ' ')

print(res_list[-1])