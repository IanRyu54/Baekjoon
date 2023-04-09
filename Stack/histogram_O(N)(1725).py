import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
squares = [int(input()) for _ in range(num)]

result = 0
heights = []
ind = []
max_height = 0
temp = 0

for i in range(len(squares)):
    if(squares[i] > max_height):
        heights.append(squares[i])
        ind.append(i)
    else:
        leng = len(heights)
        temp = 0
        for j in range(1, leng + 1):
            if(heights[-1] < squares[i]):
                break
            
            ind.pop()

            if(j < leng):
                temp = max(temp, (i - ind[-1] - 1) * heights.pop())
            else:
                temp = max(temp, i * heights.pop())

        result = max(result, temp)
        heights.append(squares[i])
        ind.append(i)
    max_height = squares[i]

leng = len(heights)
for j in range(leng):
    if(j < leng - 1):
        ind.pop()
        temp = max(temp, (i - ind[-1]) * heights.pop())
    else:
        temp = max(temp, (i + 1) * heights.pop())

result = max(result, temp)
    
print(result)