import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

num_V, num_E = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(num_E)]
adj = [[] for _ in range(num_V)]
visited = [0 for _ in range(num_V)]
result = 0

def find_connect(ind):
    visited[ind] = 1
    for i in range(len(adj[ind])):
        if(not visited[adj[ind][i]]):
            find_connect(adj[ind][i])
    return

for i in lines:
    adj[i[0] - 1].append(i[1] - 1)
    adj[i[1] - 1].append(i[0] - 1)

for i in range(len(adj)):
    if(not visited[i]):
        find_connect(i)
        result += 1
        
print(result)