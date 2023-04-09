import sys
import copy

sys.stdin = open('input.txt', 'r')

num = int(input())

candy = [0 for _ in range(num**2)]

for i in range(num):
    num_temp = input()
    
    for j in range(num):
        if(num_temp[j] == "C"):
            candy[i*num+j] = 1
        elif(num_temp[j] == "P"):
            candy[i*num+j] = 2
        elif(num_temp[j] == "Z"):
            candy[i*num+j] = 3
        else:
            candy[i*num+j] = 4

locx = [1 for _ in range(num**2)]
locy = [1 for _ in range(num**2)]

for i in range(num**2):
    if(i-1>=0 and divmod(i-1,num)[0] == divmod(i,num)[0]):
        if(candy[i] == candy[i-1]):
            locx[i] = locx[i-1] + 1
    if(i-num>=0):
        if(candy[i] == candy[i-num]):
            locy[i] = locy[i-num] + 1

temp = ""
result = 1
temp_num = 1

for i in range(1,num**2):
    if(candy[i]!=candy[i-1] and divmod(i,num)[0]==divmod(i-1,num)[0]):
        temp_candy = copy.deepcopy(candy)
        temp_locx = copy.deepcopy(locx)
        temp_locy = copy.deepcopy(locy)

        temp = temp_candy[i]
        temp_candy[i] = temp_candy[i-1]
        temp_candy[i-1] = temp

        for k in range(divmod(i,num)[0]*num,(divmod(i,num)[0]+1)*num):
            temp_locx[k] = 1
            if(k-1>=0 and divmod(k-1,num)[0] == divmod(k,num)[0]):
                if(temp_candy[k] == temp_candy[k-1]):
                    temp_locx[k] = temp_locx[k-1] + 1
        for k in range(num):
            tempk = k*num + divmod(i,num)[1]
            temp_locy[tempk] = 1
            if(tempk-num>=0):
                if(temp_candy[tempk] == temp_candy[tempk-num]):
                    temp_locy[tempk] = temp_locy[tempk-num] + 1
            tempk = k*num + divmod(i,num)[1] - 1
            temp_locy[tempk] = 1
            if(tempk-num>=0):
                if(temp_candy[tempk] == temp_candy[tempk-num]):
                    temp_locy[tempk] = temp_locy[tempk-num] + 1
        temp_num = max(max(temp_locx),max(temp_locy))

        if(result < temp_num):
            result = temp_num
    if(candy[i]!=candy[i-num] and i-num>=0):
        temp_candy = copy.deepcopy(candy)
        temp_locx = copy.deepcopy(locx)
        temp_locy = copy.deepcopy(locy)

        temp = temp_candy[i]
        temp_candy[i] = temp_candy[i-num]
        temp_candy[i-num] = temp

        for k in range((divmod(i,num)[0]-1)*num,(divmod(i,num)[0]+1)*num):
            temp_locx[k] = 1
            if(k-1>=0 and divmod(k-1,num)[0] == divmod(k,num)[0]):
                if(temp_candy[k] == temp_candy[k-1]):
                    temp_locx[k] = temp_locx[k-1] + 1
        for k in range(num):
            tempk = k*num + divmod(i,num)[1]
            temp_locy[tempk] = 1
            if(tempk-num>=0):
                if(temp_candy[tempk] == temp_candy[tempk-num]):
                    temp_locy[tempk] = temp_locy[tempk-num] + 1
        temp_num = max(max(temp_locx),max(temp_locy))
        
        if(result < temp_num):
            result = temp_num
            
print(result)