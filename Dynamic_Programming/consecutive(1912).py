import sys

sys.stdin = open('input.txt', 'r')

length = int(input())
sum_list = list(map(int,input().split()))

k=-1
ind = 0
temp = 0

if(max(sum_list)<0):
    print(max(sum_list))
else:
    """for i in range(length):
        if(data[i]>=0):
            if(k==-1):
                temp = data[i]
                k=1
            elif(k==0):
                sum_list[ind] = temp
                ind = ind+1
                temp = data[i]
                k=1
            else:
                temp = temp + data[i]
        else:
            if(k==1):
                sum_list[ind] = temp
                ind = ind+1
                temp = data[i]
                k=0
            else:
                temp = temp+data[i]

    sum_list[ind] = temp
    length_change = length

    for i in range(length-1):
        if(sum_list[i]==0 and sum_list[i+1]==0):
            length_change = i
            break"""
    
    sum = [0 for _ in range(length)]
    
    for i in range(length):
        if(i==0):
            sum[i] = sum_list[i]
        else:
            sum[i] = max(sum[i-1]+sum_list[i],sum_list[i])

    print(max(sum))