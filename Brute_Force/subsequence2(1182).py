import copy
import sys

sys.stdin = open('input.txt', 'r')

def summing(resu, num, seq):
    if(len(seq) > 1):
        resu = resu + divmod(num,2)[1] * seq[0] 
        return summing(resu,divmod(num,2)[0],seq[1:])
    else:
        return resu + divmod(num,2)[1] * seq[0]

number, sum_result = map(int,input().split())
sequence = list(map(int,input().split()))

sequence = sorted(sequence)

on_num = 2 ** number
switch = [0 for _ in range(number)]

result = 0
seq_sum = 0
i = 0

for i in range(1, on_num):
    temp = summing(seq_sum, i, sequence)
    if(temp == sum_result):
        result = result + 1

print(result)