import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

goal, p, q, x, y = map(int, input().split())

dict = {0: 1}

def dividing(num):
    if(num < 0):
        num = 0
    if(dict.get(num) != None):
        return dict[num]
    else:
        res = dividing(num // p - x) + dividing(num // q - y)
        dict[num] = res
        return res
    
print(dividing(goal))