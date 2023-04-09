import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

number = int(input())

time = [number for _ in range(number + 1)]

time[0] = 0
time[1] = 0

for i in range(1,number + 1):
    if(i + 1 < number + 1):
        time[i + 1] = min(time[i] + 1, time[i + 1])
    if(2 * i < number + 1):
        time[2 * i] = min(time[i] + 1, time[2 * i])
    if(3 * i < number + 1):
        time[3 * i] = min(time[i] + 1, time[3 * i])

print(time[number])