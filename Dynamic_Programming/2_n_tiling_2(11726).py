import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

lengths = int(input())

result = 1
result_bef = 3
result_bebe = 1

for i in range(lengths - 1):
    if(i == 0):
        result = result_bef
    else:
        result = (result_bebe * 2 + result_bef) % 10007
        result_bebe = result_bef
        result_bef = result
        
print(result)