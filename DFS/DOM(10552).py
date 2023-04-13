import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num_pensionier, num_channel, now_channel = map(int, input().split())
pensioniers = [list(map(int, input().split())) for _ in range(num_pensionier)]
visited = [0 for _ in range(num_channel + 1)]
arrows = {}

for i in range(num_pensionier):
    if(pensioniers[i][1] not in arrows):
        arrows[pensioniers[i][1]] = pensioniers[i][0]
        
result = 0
while(True):
    if(now_channel in arrows):
        if(not visited[now_channel]):
            result += 1
            visited[now_channel] = 1
            now_channel = arrows[now_channel]
        else:
            result = -1
            break
    else:
        break

print(result)