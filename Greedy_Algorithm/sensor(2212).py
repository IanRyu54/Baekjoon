import sys

sys.stdin = open('input.txt', 'r')

sensor_num = int(input())
site_num = int(input())
site_loc = list(map(int,input().split()))

site_loc.sort()

site_dist = []

for i in range(len(site_loc) - 1):
    site_dist.append(site_loc[i + 1] - site_loc[i])

result = 0
site_dist.sort(reverse=True)

for i in range(site_num-1):
    if(len(site_dist)>0):
        del site_dist[0]

for i in site_dist:
    result = result + i
    
print(result)