import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
expr = input().split("\n")[0]
numbers = [int(input()) for _ in range(num)]

temp = []

for i in expr:
    if(i == "*"):
        temp.append(temp.pop() * temp.pop())
    elif(i == "/"):
        temp.append((1 / temp.pop()) * temp.pop())
    elif(i == "+"):
        temp.append(temp.pop() + temp.pop())
    elif(i == "-"):
        temp.append(- temp.pop() + temp.pop())
    else:
        temp.append(numbers[ord(i) - 65])

print("{:.2f}".format(temp[0]))