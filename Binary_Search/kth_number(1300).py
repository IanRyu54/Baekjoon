import sys

input = sys.stdin.readline

lengths = int(input())
number = int(input())

min_num = 0
max_num = min(10 ** 9, lengths ** 2) + 1

while(max_num - min_num > 1):
    cut = (max_num + min_num) // 2
    low_tot = 0
    high_tot = 0

    for i in range(1, lengths + 1):
        temp = min(cut // i, lengths)
        low_tot += temp
        if(lengths * i > cut):
            temp = min((lengths * i - cut) // i + 1, lengths)
            high_tot += temp
    
    if(low_tot < number):
        min_num = cut
    else:
        max_num = cut
        if(high_tot > lengths ** 2 - number):
            break

print(max_num)