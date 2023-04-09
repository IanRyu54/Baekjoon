import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num, length = map(int, input().split())
heights = list(map(int,input().split()))

start = 0
end = max(heights)
result = 0

while(end - start > 1):
    cut = (start + end) // 2
    sum = 0
    for i in heights:
        taken = i - cut
        if(taken >= 0):
            sum += taken
        if(sum >= length):
            start = cut
            break
    if(sum < length):
        end = cut

print(start)