import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

days, withdraw = map(int, input().split())
moneys = [int(input()) for _ in range(days)]

start = max(moneys) - 1
end = sum(moneys)

while(end - start > 1):
    cut = (start + end) // 2
    num = 1
    sum = 0

    for i in moneys:
        sum += i
        if(sum > cut):
            num += 1
            sum = i

    if(num > withdraw):
        start = cut
    else:
        end = cut
        
print(end)