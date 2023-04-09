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

temp = ""
result = 1
temp_num = 1

for i in range(1,num**2):
    locx = [1 for _ in range(num**2)]
    locy = [1 for _ in range(num**2)]
    if(candy[i]!=candy[i-1] and divmod(i,num)[0]==divmod(i-1,num)[0]):
        temp_candy = copy.deepcopy(candy)

        temp = temp_candy[i]
        temp_candy[i] = temp_candy[i-1]
        temp_candy[i-1] = temp

        for j in range(num**2):
            if(j-1>=0 and divmod(j-1,num)[0] == divmod(j,num)[0]):
                if(temp_candy[j] == temp_candy[j-1]):
                    locx[j] = locx[j-1] + 1
            if(j-num>=0):
                if(temp_candy[j] == temp_candy[j-num]):
                    locy[j] = locy[j-num] + 1
                    
        temp_num = max(max(locx),max(locy))
        
        if(result < temp_num):
            result = temp_num

    locx = [1 for _ in range(num**2)]
    locy = [1 for _ in range(num**2)]

    if(candy[i]!=candy[i-num] and i-num>=0):
        temp_candy = copy.deepcopy(candy)

        temp = temp_candy[i]
        temp_candy[i] = temp_candy[i-num]
        temp_candy[i-num] = temp

        for j in range(num**2):
            if(j-1>=0 and divmod(j-1,num)[0] == divmod(j,num)[0]):
                if(temp_candy[j] == temp_candy[j-1]):
                    locx[j] = locx[j-1] + 1
            if(j-num>=0):
                if(temp_candy[j] == temp_candy[j-num]):
                    locy[j] = locy[j-num] + 1
                    
        temp_num = max(max(locx),max(locy))
        
        if(result < temp_num):
            result = temp_num
            
print(result)