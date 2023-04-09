import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num, length = map(int,input().split())
videos = list(map(int,input().split()))

end = sum(videos)
start = 0

while(end - start > 1):
    cut = (start + end) // 2
    k = 1
    temp = 0
    for i in videos:
        temp += i
        if(cut < temp):
            k += 1
            temp = i
    if(k > length):
        start = cut
    else:
        end = cut

if(end < max(videos)):
    end = max(videos)

print(end)