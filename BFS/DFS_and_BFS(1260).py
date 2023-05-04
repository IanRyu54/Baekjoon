import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

dots, edges, start = map(int, input().split())
dot_list = [list(map(int, input().split())) for _ in range(edges)]
adj_list = [[] for _ in range(dots)]
visited_dfs = [0 for _ in range(dots)]
visited_bfs = visited_dfs[:]

def find_adj():
    for i in dot_list:
        adj_list[i[0] - 1].append(i[1] - 1)
        adj_list[i[1] - 1].append(i[0] - 1)
    
    for i in range(len(adj_list)):
        adj_list[i].sort()

def do_dfs(ind):
    visited_dfs[ind] = 1
    print(ind + 1, end = ' ')
    for i in adj_list[ind]:
        if(not visited_dfs[i]):
            visited_dfs[i] = 1
            do_dfs(i)

def do_bfs():
    now_dot = deque([start - 1])
    visited_bfs[start - 1] = 1
    while(now_dot):
        for i in range(len(now_dot)):
            cur_dot = now_dot[0]
            print(cur_dot + 1, end = ' ')
            now_dot.popleft()
            for j in adj_list[cur_dot]:
                if(not visited_bfs[j]):
                    visited_bfs[j] = 1
                    now_dot.append(j)

find_adj()
do_dfs(start - 1)
print()
do_bfs()