import copy
import sys

sys.stdin = open('input.txt', 'r')

number, sum_result = map(int,input().split())
sequence = list(map(int,input().split()))

on_off = 2**number
result = 0
seq_sum = sum(sequence)

if(sum_result in sequence):
    for i in range(on_off-1):
        sum_temp = seq_sum
        temp = i

        for j in range(len(sequence)):
            sum_temp = sum_temp - sequence[j]*divmod(temp,2)[1]
            temp = divmod(temp,2)[0]
        
        if(sum_result == sum_temp):
            result = result + 1
else:
    for i in range(on_off-1):
        sum_temp = seq_sum
        temp = i

        for j in range(len(sequence)):
            sum_temp = sum_temp - sequence[j]*divmod(temp,2)[1]
            temp = divmod(temp,2)[0]
        
        if(sum_result == sum_temp):
            result = result + 1

print(result)