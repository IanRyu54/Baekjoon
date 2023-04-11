import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

def find_path(ind):
    for i in paths[ind]:
        if(not visited[i]):
            visited[i] = 1
            find_path(i)

num = int(input())
paths = [[] for _ in range(num)]

for i in range(num):
    ind = 0
    for j in map(int, input().split()):
        if(j):
            paths[i].append(ind)
        ind += 1

for i in range(num):
    visited = [0 for _ in range(num)]
    find_path(i)
    print(' '.join(list(map(str, visited))))