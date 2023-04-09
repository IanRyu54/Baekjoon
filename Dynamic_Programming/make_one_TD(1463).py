import sys
import os

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

number = int(input())

time = [-1 for _ in range(number + 1)]

def times(nums):
    if(nums == 1):
        time[nums] = 0
        return 0
    if(nums == 2):
        time[nums] = 1
        return 1
    if(time[nums] != -1):
        return time[nums]
    else:
        result = min(times(nums // 3) + nums % 3, times(nums // 2) + nums % 2) + 1
    time[nums] = result
    return result
    

result = times(number)

print(result)