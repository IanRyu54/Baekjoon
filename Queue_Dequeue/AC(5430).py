from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
orders = []
for _ in range(num):
    temp = []
    temp.append(input().split("\n")[0])
    num_arr = int(input())
    temp1 = []
    if(num_arr):
        temp1 = deque(list(map(int, input().strip("]\n").strip("[").split(","))))
    else:
        input()
    temp.append(temp1)
    orders.append(temp)

for i in orders:
    now = i[1]
    err = 0
    from_where = True
    for j in i[0]:
        if(j == "R"):
            from_where = not from_where
        else:
            try:
                if(from_where):
                    now.popleft()
                else:
                    now.pop()
            except:
                err = 1
    if(err):
        print("error")
    else:
        if(from_where):
            print(''.join(str(list(now)).split()))
        else:
            print(''.join(str(list(now)[::-1]).split()))