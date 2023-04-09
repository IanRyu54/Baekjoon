import sys

sys.stdin = open('input.txt', 'r')

tot_num = int(input())
homeworks = [list(map(int,input().split())) for _ in range(tot_num)]

homeworks.sort(reverse=True)
max_days = homeworks[0][0]

homeworks.sort(key=lambda x : x[1], reverse=True)

schedule = [0 for _ in range(max_days)]

for i in homeworks:
    for j in range(i[0]):
        loc = i[0] - j - 1
        if(schedule[loc] == 0):
            schedule[loc] = i[1]
            break

result = 0

for i in schedule:
    result = result + i

print(result)