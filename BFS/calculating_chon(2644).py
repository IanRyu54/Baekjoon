import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

people_num = int(input())
chon1, chon2 = map(int, input().split())
chons = int(input())
chon_list = [list(map(int, input().split())) for _ in range(chons)]

adj_list = [[] for _ in range(people_num)]
visited = [0 for _ in range(people_num)]

for i in chon_list:
    adj_list[i[0] - 1].append(i[1] - 1)

for i in chon_list:
    adj_list[i[1] - 1].append(i[0] - 1)

people = deque([])
people.append(chon1 - 1)
result = 0
found = 0
while(people):
    for i in range(len(people)):
        temp = people[0]
        people.popleft()
        for j in adj_list[temp]:
            if(j == chon2 - 1):
                found = 1
                people = []
                break
            if(not visited[j]):
                visited[j] = 1
                people.append(j)
    result += 1

if(found):
    print(result)
else:
    print(-1)