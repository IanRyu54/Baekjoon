import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

def scissor (lists):
    leng = len(lists)
    subleng = leng // 3
    temp_ret = [0, 0, 0]
    nums = [0, 0, 0]
    if(leng == 1):
        temp_ret[lists[0][0] + 1] += 1
        return temp_ret

    for i in range(3):
        for j in range(3):
            temp = []
            for k in range(subleng):
                temp.append(lists[subleng * i + k][subleng * j : subleng * j + subleng])
            temp_ret = scissor(temp)
            nums = [nums[i] + temp_ret[i] for i in range(len(nums))]
    k = 0
    for i in nums:
        if(i == 9 or i == 0):
            k = k + 1
    if(k == 3):
        nums = [i // 9 for i in nums]
    return nums
    

length = int(input())

paper = [list(map(int,input().split())) for _ in range(length)]

numbers = scissor(paper)
print(numbers[0])
print(numbers[1])
print(numbers[2])