import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

def find_path(start, end):
    global visited
    global success
    for i in range(num):
        success = 0
        if(paths[start][i]):
            visited[i] = 1
            success = finding(start, i, end)
            for j in range(num):
                visited[j] = 0
        if(success):
            paths[start][end] = 1
            break

def finding(start, via, end):
    global success
    for i in range(num):
        if(not visited[i]):
            if(paths[via][i]):
                if(i == end):
                    return 1
                else:
                    visited[i] = 1
                    success = finding(start, i, end)
        if(success == 1):
            break
    return success

num = int(input())
paths = [list(map(int, input().split())) for _ in range(num)]
visited = [0 for _ in range(num)]
success = 0

for i in range(num):
    for j in range(num):
        if(not paths[i][j]):
            find_path(i, j)

for i in paths:
    print(' '.join(list(map(str, i))))