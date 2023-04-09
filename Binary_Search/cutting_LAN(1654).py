import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num, cut = map(int, input().split())
lengths = [int(input()) for _ in range(num)]

start = 0
end = max(lengths) + 1

while(end - start > 1):
    ind = (start + end) // 2
    sum = 0
    
    for i in lengths:
        sum += i // ind

    if(sum >= cut):
        start = ind
    else:
        end = ind
        
print(start)