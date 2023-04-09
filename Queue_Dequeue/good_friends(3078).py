from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num, grade = map(int, input().split())
friends = [input().split("\n")[0] for _ in range(num)]
temp = [deque([]) for _ in range(21)]
result = 0

for i in range(num - 1):
    if(i == 0):
        for j in range(1, grade + 1):
            temp[len(friends[j])].append(j)
        result += len(temp[len(friends[i])])
        temp[len(friends[i + 1])].popleft()
    else:
        if(i < num - grade):
            ind1 = len(friends[i + grade])
            temp[ind1].append(i + grade)
        result += len(temp[len(friends[i])])
        temp[len(friends[i + 1])].popleft()

print(result)