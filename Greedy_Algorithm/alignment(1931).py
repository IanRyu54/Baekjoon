import sys

sys.stdin = open('input.txt','r')

number = int(input())
meeting = [list(map(int,input().split())) for _ in range(number)]

meeting.sort()
meeting.sort(key = lambda x : x[1])

end_loc = 0
result = 0

for i in meeting:
    if(i[0] >= end_loc):
        end_loc = i[1]
        result = result + 1

print(result)