import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

size = int(input())
num_apple = int(input())
apple_loc = [list(map(int, input().split())) for _ in range(num_apple)]
change_num = int(input())
dir_list = [list(input().split()) for _ in range(change_num)]

for i in range(len(dir_list)):
    dir_list[i][0] = int(dir_list[i][0])

dir_list.append([dir_list[-1][0] + size, ""])

dead = 0
dire = 2
time = 1
order = 0
snake_len = 1
path = [[1, 1]]

while(True):
    coeff = ((dire - dire % 2) - 1)
    path.append([path[-1][0] + coeff * (dire % 2), path[-1][1] + coeff * ((dire + 1) % 2)])
    
    if(path[-1][0] > size or path[-1][1] > size or path[-1][0] <= 0 or path[-1][1] <= 0):
        dead = 1

    for i in range(len(path) - 1):
        if(path[i] == path[-1]):
            if(len(path) - i <= snake_len + 1):
                dead = 1
                break

    for i in apple_loc:
        if(path[-1] == i):
            apple_loc.remove(i)
            snake_len += 1
    
    if(dir_list[order][0] == time):
        if(dir_list[order][1] == "D"):
            dire += 1
        else:
            dire -= 1
        dire %= 4
        order += 1

    if(dead == 1):
        break

    time += 1

print(time)