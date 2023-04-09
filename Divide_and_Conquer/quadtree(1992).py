import sys
import os

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

def compress(lists):
    result = ""
    leng = len(lists)
    subleng = leng // 2

    if(len(lists) == 1):
        nums = [0, 0]
        nums[lists[0][0]] += 1
        comp = lists[0][0]
        comp = str(comp)
        return comp, nums

    nums = [0, 0]
    comp = ""

    for i in range(2):
        for j in range(2):
            temp = []

            for k in range(subleng):
                temp.append(lists[subleng * i + k][subleng * j : subleng * j + subleng])

            temp, temp_ret = compress(temp)
            nums = [nums[i] + temp_ret[i] for i in range(len(nums))]
            comp = comp + temp

    k = 0

    for i in nums:
        if(i == 0 or i == 4):
            k += 1

    if(k == 2):
        comp = comp[0]
        nums = [i // 4 for i in nums]
    else:
        comp = "(" + comp + ")"

    return comp, nums

length = int(input())

trees = [list(input()) for _ in range(length)]

for i in range(len(trees)):
    for j in range(len(trees)):
        trees[i][j] = int(trees[i][j])

result, temp = compress(trees)    

print(result)