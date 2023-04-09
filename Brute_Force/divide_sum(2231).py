import sys

sys.stdin = open('input.txt', 'r')

def divsum (sum, i):
    if(divmod(i,10)[0]!=0):
        return divsum(sum,divmod(i,10)[0]) + divmod(i,10)[1]
    else:
        return sum + divmod(i,10)[1]

num = int(input())
result = float("inf")

temp = num
length = 1

for i in range(1,num+1):
    sum = 0
    sum = sum + i
    result = i
    sum = divsum(sum,i)
    if(sum == num):
        break

if(result == num):
    result = 0

print(result)