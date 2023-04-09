import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

case_num = int(input())
cases = [int(input()) for _ in range(case_num)]

fib = [[1, 0], [0, 1]]
len = 2

for i in cases:
    if(len <= i):
        for j in range(len, i + 1):
            fib.append([fib[j - 1][0] + fib[j - 2][0], fib[j - 1][1] + fib[j - 2][1]])
        len = i + 1
        
    print(fib[i][0], end = ' ')
    print(fib[i][1])