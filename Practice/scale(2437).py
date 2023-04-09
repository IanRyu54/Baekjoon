import sys
import os

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())

weight = list(map(int,input().split()))
weight.sort()

sum = 0
for i in weight:
    if(i <= sum + 1):
        sum += i

print(sum + 1)