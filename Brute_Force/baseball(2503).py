import copy
import sys

sys.stdin = open('input.txt', 'r')

length = int(input())

numbers = []

for i in range(123,988):
    if (divmod(i,100)[0]!=divmod(divmod(i,100)[1],10)[0] and divmod(divmod(i,100)[1],10)[0]!=divmod(divmod(i,100)[1],10)[1] and divmod(divmod(i,100)[1],10)[1]!=divmod(i,100)[0] and divmod(i,100)[0]!=0 and divmod(divmod(i,100)[1],10)[0]!=0 and divmod(divmod(i,100)[1],10)[1]!=0):
        numbers.append(i)

temp_num = copy.deepcopy(numbers)
result = []

for i in range(length):
    number, strike, ball = map(int,input().split())
    hundred = divmod(number,100)[0]
    tens = divmod(divmod(number,100)[1],10)[0]
    ones = divmod(divmod(number,100)[1],10)[1]
    temp_result = []
    t_result = []

    for j in temp_num:
        strike_num = 0
        ball_num = 0
        hundred_num = divmod(j,100)[0]
        tens_num = divmod(divmod(j,100)[1],10)[0]
        ones_num = divmod(divmod(j,100)[1],10)[1]
        if(hundred == hundred_num):
            strike_num = strike_num + 1
        if(hundred == tens_num or hundred == ones_num):
            ball_num = ball_num + 1
        if(tens == tens_num):
            strike_num = strike_num + 1
        if(tens == hundred_num or tens == ones_num):
            ball_num = ball_num + 1
        if(ones == ones_num):
            strike_num = strike_num + 1
        if(ones == hundred_num or ones == tens_num):
            ball_num = ball_num + 1
        if(strike == strike_num and ball == ball_num):
            temp_result.append(j)
    
    if(len(result)==0):
        result = temp_result
    else:
        for j in temp_result:
            if(j in result):
                t_result.append(j)
        result = []
        result = t_result

print(len(result))