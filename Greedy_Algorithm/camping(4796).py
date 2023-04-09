import copy
import sys

sys.stdin = open('input.txt', 'r')

case_num = 0

while(True):
    case_num = case_num + 1
    camp = list(map(int,input().split()))

    if(camp[0] == 0):
        break

    tot_period = divmod(camp[2], camp[1])[0]
    result = tot_period * camp[0] + min(divmod(camp[2], camp[1])[1], camp[0])

    print("Case " + str(case_num) +": " + str(result))