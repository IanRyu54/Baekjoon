import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

goal, p, q = map(int, input().split())

dict = {0: 1}

def dividing(num):
    if(dict.get(num) != None):
        return dict[num]
    else:
        res = dividing(num // p) + dividing(num // q)
        dict[num] = res
        return res
    
print(dividing(goal))