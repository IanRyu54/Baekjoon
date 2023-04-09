import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

expr = input().split("\n")[0]
result = ""
temp = [[] for _ in range(100000)]
level = 0

for i in expr:
    if(i == "+" or i == "-"):
        while(temp[level]):
            result += temp[level].pop()
        if(level % 2 == 1):
            level -= 1
        while(temp[level]):
            result += temp[level].pop()
        temp[level].append(i)
    elif(i == "*" or i == "/"):
        if(level % 2 == 0):
            level += 1
        else:
            while(temp[level]):
                result += temp[level].pop()
        temp[level].append(i)
    elif(i == "("):
        level += 2
    elif(i == ")"):
        while(temp[level]):
            result += temp[level].pop()
        if(level % 2 == 1):
            level -= 1
            while(temp[level]):
                result += temp[level].pop()
        level -= 1
    else:
        result += i

while(level >= 0):
    while(temp[level]):
        result += temp[level].pop()
    level -= 1

print(result)