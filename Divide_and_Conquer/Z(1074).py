import sys
import os

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

def whereisnum(rows, columns, nums, order):
    if(nums == 0):
        return order
    
    half = nums - 1
    if(rows < 2 ** half):
        if(columns < 2 ** half):
            result = whereisnum(rows, columns, half, order)
        else:
            order += (2 ** half) ** 2
            result = whereisnum(rows, columns - (2 ** half), half, order)
    else:
        if(columns < 2 ** half):
            order += ((2 ** half) ** 2) * 2
            result = whereisnum(rows - (2 ** half), columns, half, order)
        else:
            order += ((2 ** half) ** 2) * 3
            result = whereisnum(rows - (2 ** half), columns - (2 ** half), half, order)
    return result

length, row, column = map(int,input().split())

order = 0
result = whereisnum(row, column, length, order)

print(result)