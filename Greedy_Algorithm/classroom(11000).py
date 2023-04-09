import sys

sys.stdin = open('input.txt', 'r')

number = int(input())

classes = [list(map(int,input().split())) for _ in range(number)]

result = 0
end_loc = []
start = 0
end = 0

classes.sort()

for i in classes:
    if(len(end_loc) == 0):
        end_loc.append(i[1])
    else:
        if(i[1] >= end_loc[-1]):
            end_loc.append(i[1])
        else:
            for j in range(len(end_loc)):
                if(i[1] <= end_loc[j]):
                    end_loc.insert(j,i[1])
                    break
        if(i[0] >= end_loc[0]):
            del end_loc[0]

print(len(end_loc))