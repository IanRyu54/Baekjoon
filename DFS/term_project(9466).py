import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

num = int(input())

def project(ind):
    global result
    visited[ind] = 1
    next = students[ind] - 1

    if(not visited[next]):
        project(next)
    else:
        while(not finished[next]):
            result += 1
            finished[next] = 1
            next = students[next] - 1
    
    finished[ind] = 1

for _ in range(num):
    num_student = int(input())
    students = list(map(int, input().split()))
    visited = [0 for _ in range(num_student)]
    finished = [0 for _ in range(num_student)]
    result = 0
    leng = len(students)

    for j in range(leng):
        if(not visited[j]):
            project(j)
            
    print(leng - result)