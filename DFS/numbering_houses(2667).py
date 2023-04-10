import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

direc = [[0, -1], [0, 1], [-1, 0], [1, 0]]
def visit_house(loc):
    visited[loc[1]][loc[0]] = 1
    for i in direc:
        new_x = loc[0] + i[0]
        new_y = loc[1] + i[1]
        if(new_x >= 0 and new_y >= 0 and new_x < length and new_y < length and not visited[new_y][new_x] and maps[new_y][new_x]):
            num_house[-1] += 1
            visit_house([new_x, new_y])

length = int(input())
maps = [list(map(int, list(input().strip("\n")))) for _ in range(length)]
visited = [[0 for _ in range(length)] for _ in range(length)]
num_house = []

x = 0
y = 0

for i in maps:
    x = 0
    for j in i:
        if(j and not visited[y][x]):
            num_house.append(1)
            visit_house([x, y])
        x += 1
    y += 1

num_house.sort()
print(len(num_house))
for i in num_house:
    print(i)