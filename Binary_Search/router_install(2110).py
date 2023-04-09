import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

house, router = map(int, input().split())
coord = [int(input()) for _ in range(house)]
coord.sort()

min_dist = 0
max_dist = (coord[-1] - coord[0]) // (router - 1) + 1

while(max_dist - min_dist > 1):
    cut = (min_dist + max_dist) // 2
    install = 1
    tot = 0
    temp = coord[0]
    for i in coord:
        res = i - temp
        tot += res
        temp = i
        if(tot > cut):
            tot = 0
            install += 1
    
    if(install >= router):
        min_dist = cut
    else:
        max_dist = cut

print(max_dist)