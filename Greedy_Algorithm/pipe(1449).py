import copy
import sys

sys.stdin = open('input.txt', 'r')

number, length = map(int,input().split())
location = list(map(int,input().split()))

new = 0
result = 0

location = sorted(location)

for i in location:
    if(new == 0):
        temp = i
        new = 1
        result = result + 1
    else:
        if(i >= temp + length):
            temp = i
            result = result + 1

print(result)