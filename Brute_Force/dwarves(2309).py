import sys

sys.stdin = open('input.txt', 'r')

height = [0 for _ in range(9)]

for i in range(len(height)):
    height[i] = int(input())

sum = 0

for i in range(len(height)):
    sum = sum + height[i]

answer_found = 0
answer = [0 for _ in range(len(height)-2)]

for i in range(len(height)):
    for j in range(i+1,len(height)):
        temp = sum
        temp = temp - height[i]
        temp = temp - height[j]
        if(temp == 100):
            temp1 = 0
            for k in range(len(height)):
                if(k!=i and k!=j):
                    answer[temp1] = height[k]
                    answer_found = 1
                    temp1 = temp1+1
        if(answer_found == 1):
            break
    if(answer_found == 1):
        break

for i in range(len(answer)):
    print(sorted(answer)[i])