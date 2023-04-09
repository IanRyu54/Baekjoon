import sys
import math

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

number = int(input())
number_res = [100000 for _ in range(number + 1)]
number_res[0] = 0

for i in range(1, number + 1):
    for j in range(1, i + 1): 
        if(j ** 2 > i):
            break

        temp = 1
        temp += number_res[i - j ** 2]

        if(temp < number_res[i]):
            number_res[i] = temp

print(number_res[number])