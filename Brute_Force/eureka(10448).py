import sys

sys.stdin = open('input.txt', 'r')

length = int(input())

triangular = []

for i in range(1,1000):
    temp = 0
    temp = int(i*(i+1)/2)

    if(temp >1000):
        break

    triangular.append(temp)

for i in range(length):
    found = 0

    tri = int(input())

    for j in triangular:
        if(j>tri):
            break

        for k in triangular:
            if(k>tri):
                break

            for p in triangular:
                if(p>tri):
                    break
                if(j+k+p == tri):
                    found = 1
                    break

            if(found == 1):
                break

        if(found == 1):
            break

    print(found)