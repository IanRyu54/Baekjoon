import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

alph_num, rotate_num = map(int, input().split())
alphabets = [list(input().split()) for _ in range(rotate_num)]
wheels = ["?" for _ in range(alph_num)]

for i in range(len(alphabets)):
    alphabets[i][0] = int(alphabets[i][0])

ind = 0
for i in alphabets:
    ind -= i[0]
    ind %= alph_num

    if(wheels[ind] == "?" or wheels[ind] == i[1]):
        if(i[1] in wheels and wheels.index(i[1]) != ind):
            ind = -1
        wheels[ind] = i[1]
    else:
        ind = -1

    if(ind == -1):
        print("!")
        break

if(ind != -1):
    for i in wheels:
        print(wheels[ind], end = "")
        ind +=1
        ind %= alph_num