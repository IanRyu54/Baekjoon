import sys
import os

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num, attack = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(num)]

min_HP = 0
max_HP = 0
for i in rooms:
    if(i[0] == 1):
        max_HP += i[1] * (i[2] // attack)
max_HP += 1

while(max_HP - min_HP > 1):
    cut_HP = (min_HP + max_HP) // 2
    cur_HP = cut_HP
    cur_att = attack
    for i in rooms:
        if(i[0] == 1):
            cur_HP -= i[1] * (i[2] // cur_att)
            if(i[2] % cur_att == 0):
                cur_HP += i[1]
            if(cur_HP <= 0):
                break
        else:
            cur_HP += i[2]
            if(cur_HP > cut_HP):
                cur_HP = cut_HP
            cur_att += i[1]

    if(cur_HP <= 0):
        min_HP = cut_HP
    else:
        max_HP = cut_HP

print(max_HP)