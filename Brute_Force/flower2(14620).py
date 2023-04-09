import sys
import copy

sys.stdin = open('input.txt', 'r')

length = int(input())
data = [list(map(int,input().split())) for _ in range(length)]

total_money = float("inf");
sum_money = [[0 for _ in range(length)] for _ in range(length)]

for i in range(length):
    for j in range(length):
        if(i==0 or j==0 or i==length-1 or j==length-1):
            sum_money[i][j] = float("inf")
        else:
            sum_money[i][j] = data[i][j] + data[i-1][j] + data[i][j-1] + data[i+1][j] + data[i][j+1]



print(total_money)