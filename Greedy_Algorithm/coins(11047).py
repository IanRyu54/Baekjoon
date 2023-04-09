import sys

sys.stdin = open("input.txt","r")

number, total = map(int,input().split())
values = list(int(input()) for _ in range(number))

result = 0
temp = total
values.sort(reverse = True)

for i in values:
    result = result + divmod(temp,i)[0]
    temp = divmod(temp,i)[1]

print(result)