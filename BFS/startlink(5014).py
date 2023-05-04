import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

floors, from_floor, to_floor, up_num, down_num = map(int, input().split())

elevators = deque([from_floor - 1])
visited = [0 for _ in range(floors)]
visited[from_floor - 1] = 1
arrived = 0
result = 0

while(not arrived and elevators):
    for i in range(len(elevators)):
        cur_floor = elevators[0]
        elevators.popleft()

        if(cur_floor == to_floor - 1):
            result -= 1
            arrived = 1
            break

        go_up = cur_floor + up_num
        go_down = cur_floor - down_num

        if(go_up < floors):
            if(not visited[go_up]):
                visited[go_up] = 1
                elevators.append(go_up)
        
        if(go_down >= 0):
            if(not visited[go_down]):
                visited[go_down] = 1
                elevators.append(go_down)

    result += 1

if(arrived):
    print(result)
else:
    print("use the stairs")