import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
budgets = list(map(int,input().split()))
money = int(input())

sum = sum(budgets)
start = 0
end = max(budgets)
if(sum <= money):
    print(end)
else:
    while(end - start > 1):
        sum = 0
        cut = (start + end) // 2
        for i in budgets:
            taken = i - cut
            if(taken < 0):
                taken = i
            else:
                taken = cut
            sum += taken
        if(sum > money):
            end = cut
        else:
            start = cut
    print(start)