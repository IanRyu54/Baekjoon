import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

sys.setrecursionlimit(100000)

testcases = int(input())

for _ in range(testcases):
    lengths = int(input())
    stickers = [list(map(int,input().split())) for _ in range(2)]
    max_vals = [[-1 for _ in range(lengths)] for _ in range(2)]

    result = 0

    for i in range(lengths):
        if(i == 0):
            max_vals[0][i] = stickers[0][i]
            if(result < max_vals[0][i]):
                result = max_vals[0][i]
            max_vals[1][i] = stickers[1][i]
            if(result < max_vals[1][i]):
                result = max_vals[1][i]
        elif(i == 1):
            max_vals[0][i] = stickers[0][i] + max_vals[1][i - 1]
            if(result < max_vals[0][i]):
                result = max_vals[0][i]
            max_vals[1][i] = stickers[1][i] + max_vals[0][i - 1]
            if(result < max_vals[1][i]):
                result = max_vals[1][i]
        else:
            max_bef = max(max_vals[0][i - 2], max_vals[1][i - 2])
            max_vals[0][i] = max(max_vals[1][i - 1] + stickers[0][i], max_bef + stickers[0][i])
            if(result < max_vals[0][i]):
                result = max_vals[0][i]
            max_vals[1][i] = max(max_vals[0][i - 1] + stickers[1][i], max_bef + stickers[1][i])
            if(result < max_vals[1][i]):
                result = max_vals[1][i]

    print(result)