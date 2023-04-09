import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

def largest(lists, ind):
    if(len(lists) == 1):
        return lists[0]
    
    if(ind == len(lists) - 1):
        result = largest(lists[ : ind], ind//2)
    else:
        result = max(largest(lists[: ind], ind // 2), largest(lists[ind + 1 :], (len(lists) - ind)//2))
    
    vol = lists[ind]
    tot = 1
    left = ind
    right = ind
    mini = lists[ind]

    for i in range(len(lists) - 1):
        if(right + 1 < len(lists)):
            if(left - 1 >= 0):
                if(lists[left - 1] > lists[right + 1]):
                    left = left - 1
                    if(lists[left] < mini):
                        mini = lists[left]
                    tot += 1
                    temp = tot * mini
                else:
                    right = right + 1
                    if(lists[right] < mini):
                        mini = lists[right]
                    tot += 1
                    temp = tot * mini
            else:
                right = right + 1
                if(lists[right] < mini):
                    mini = lists[right]
                tot += 1
                temp = tot * mini
        else:
            left = left - 1
            if(lists[left] < mini):
                mini = lists[left]
            tot += 1
            temp = tot * mini

        if(temp > vol):
            vol = temp

    result = max(result, vol)
    return result
    
lines = int(input())
rectangle = [int(input()) for _ in range(lines)]

result = largest(rectangle, lines // 2)
print(result)