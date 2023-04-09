import sys

sys.stdin = open('input.txt', 'r')

holes, times = map(int,input().split())
orders = list(map(int, input().split()))

plugs = []
result = 0

for i in range(len(orders)):
    if(len(plugs) < holes):
        if(orders[i] not in plugs):
            plugs.append(orders[i])
    else:
        if(orders[i] not in plugs):
            temp_plugs = []

            for j in range(i+1,len(orders)):
                if(orders[j] in plugs):
                    if(len(temp_plugs) == len(plugs) - 1):
                        break
                    
                    if(orders[j] not in temp_plugs):
                        temp_plugs.append(orders[j])

            temp = 0
            
            for j in plugs:
                if(j not in temp_plugs):
                    temp = j
                    break
                
            plugs.remove(temp)
            plugs.append(orders[i])
            result = result + 1

print(result)