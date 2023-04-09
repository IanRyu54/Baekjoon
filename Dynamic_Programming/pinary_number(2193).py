import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

lengths = int(input())

number0 = 0
number1 = 1

for i in range(lengths - 1):
    temp = number1
    number1 = number0
    number0 += temp

print(number0 + number1)