import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

lengths = int(input())
result = 0
result_bef = 2
result_bebe = 1

for i in range(lengths):
    if(i == 0):
        result = result_bebe
    elif(i == 1):
        result = result_bef
    else:
        result = result_bef % 15746 + result_bebe % 15746
        result_bebe = result_bef
        result_bef = result

print(result % 15746)