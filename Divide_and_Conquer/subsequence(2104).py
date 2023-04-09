import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

def whereto (num_list, ind):
    if(len(num_list) == 1):
        return num_list[0] ** 2
    
    if(ind == len(num_list) - 1):
        result = whereto(num_list[0:ind], ind//2)
    else:
        result = max(whereto(num_list[0:ind], ind//2), whereto(num_list[ind + 1:],(len(num_list) - ind)//2))

    middle = num_list[ind] ** 2
    left = ind
    right = ind
    mini = num_list[ind]
    tot_sum = num_list[ind]
    for i in range(len(num_list) - 1):
        if(right + 1 < len(num_list)):
            if(left - 1 >= 0):
                if(num_list[left - 1] > num_list[right + 1]):
                    left = left - 1
                    if(num_list[left] < mini):
                        mini = num_list[left]
                    tot_sum += num_list[left]
                    temp = tot_sum * mini
                else:
                    right = right + 1
                    if(num_list[right] < mini):
                        mini = num_list[right]
                    tot_sum += num_list[right]
                    temp = tot_sum * mini
            else:
                right = right + 1
                if(num_list[right] < mini):
                    mini = num_list[right]
                tot_sum += num_list[right]
                temp = tot_sum * mini
        else:
            left = left - 1
            if(num_list[left] < mini):
                mini = num_list[left]
            tot_sum += num_list[left]
            temp = tot_sum * mini
        if(temp > middle):
            middle = temp
    result = max(result, middle)
    return result

num = int(input())
numbers = list(map(int, input().split()))

final_result = whereto(numbers, num//2)

print(final_result)