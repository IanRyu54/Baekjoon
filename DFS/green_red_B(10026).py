import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
def calc_areas(loc, RGB, FT):
    visited[loc[1]][loc[0]] = not visited[loc[1]][loc[0]]

    for i in dir:
        new_x = loc[0] + i[0]
        new_y = loc[1] + i[1]
        if(new_x >= 0 and new_y >= 0 and new_x < num and new_y < num):
            if(FT):
                if(visited[new_y][new_x] and RBs[new_y][new_x] == RGB):
                    calc_areas([new_x, new_y], RGB, FT)
            else:
                if(not visited[new_y][new_x] and RGBs[new_y][new_x] == RGB):
                    calc_areas([new_x, new_y], RGB, FT)

num = int(input())
RGBs = [input().strip("\n") for _ in range(num)]
RBs = []
visited = [[False for _ in range(num)] for _ in range(num)]

for i in RGBs:
    temp = ""
    for j in i:
        if(j == "B"):
            temp += j
        else:
            temp += "R"
    RBs.append(temp)

result = 0
result_RG = 0
for i in range(num):
    for j in range(num):
        if(not visited[i][j]):
            calc_areas([j, i], RGBs[i][j], False)
            result += 1

for i in range(num):
    for j in range(num):
        if(visited[i][j]):
            calc_areas([j, i], RBs[i][j], True)
            result_RG += 1

print(result, end = ' ')
print(result_RG)