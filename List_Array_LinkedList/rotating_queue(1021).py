import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

size, number = map(int, input().split())
need_nums = list(map(int, input().split()))
queues = [i for i in range(1, size + 1)]

result = 0
ind = 0

for i in need_nums:
    while(True):
        if(i == queues[0]):
            ind = 0
            del queues[0]
            break
        else:
            if(ind == 0):
                diff = queues.index(i)
                if(size - diff > diff):
                    ind = 1
                else:
                    ind = -1

            if(ind == 1):
                temp = queues[0]
                del queues[0]
                queues.append(temp)
            else:
                temp = queues.pop()
                queues.insert(0, temp)
            
            result += 1
    
    size -= 1

print(result)