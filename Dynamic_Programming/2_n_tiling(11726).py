import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

lengths = int(input())

result_bef = 2
result_bebe = 1

for i in range(lengths - 2):
    if(i % 2 == 0):
        result_bebe = (result_bebe + result_bef) % 10007
    else:
        result_bef = (result_bebe + result_bef) % 10007
        
if(lengths % 2 == 1):
    print(result_bebe)
else:
    print(result_bef)