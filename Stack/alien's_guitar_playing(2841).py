import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

tune_num, pret_num = map(int, input().split())
tunes = [list(map(int, input().split())) for _ in range(tune_num)]

pushing = [[] for _ in range(6)]
result = 0

for i in tunes:
    if(pushing[i[0] - 1]):
        while(pushing[i[0] - 1][-1] > i[1]):
            result += 1
            pushing[i[0] - 1].pop()
            if(not pushing[i[0] - 1]):
                 break
            
    if(pushing[i[0] - 1]):
        if(pushing[i[0] - 1][-1] != i[1]):
            pushing[i[0] - 1].append(i[1])
            result += 1
    else:
        pushing[i[0] - 1].append(i[1])
        result += 1

print(result)