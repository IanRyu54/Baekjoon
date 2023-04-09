import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

number = int(input())
costs = list(map(int,input().split()))

max_cost = [0 for _ in range(number)]

for i in range(number):
    for j in range(i + 1):
        max_cost[i] = max(max_cost[i], costs[i - j] + max_cost[j - 1])

print(max_cost[number - 1])