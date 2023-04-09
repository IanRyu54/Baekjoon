import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
def max_trash(loc):
    global temp
    visited[loc[0]][loc[1]] = 1
    for i in dir:
        loc_x = loc[0] + i[0]
        loc_y = loc[1] + i[1]
        if(loc_x >= 0 and loc_y >= 0 and loc_x < height and loc_y < width):
            if(trash_loc[loc_x][loc_y] == 1 and not visited[loc_x][loc_y]):
                temp += 1
                max_trash([loc_x, loc_y])
    return

height, width, num_trash = map(int, input().split())
trashes = [list(map(int, input().split())) for _ in range(num_trash)]
trash_loc = [[0 for _ in range(width)] for _ in range(height)]
visited = [[0 for _ in range(width)] for _ in range(height)]
result = 0

for i in trashes:
    trash_loc[i[0] - 1][i[1] - 1] = 1

ind = 0
temp = 0
for i in trashes:
    new_x = i[0] - 1
    new_y = i[1] - 1
    if(not visited[new_x][new_y]):
        temp = 1
        max_trash([new_x, new_y])
    if(temp > result):
        result = temp
    ind += 1

print(result)