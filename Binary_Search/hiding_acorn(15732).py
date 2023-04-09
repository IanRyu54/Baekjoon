import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

box_num, rule_num, acorn_num = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(rule_num)]
acorn = [0 for _ in range(box_num)]

max_box = box_num + 1
min_box = 0

while(max_box - min_box > 1):
    cut = (max_box + min_box) // 2
    tot = 0
    for i in rules:
        temp = cut
        if(temp > i[1]):
            temp = i[1]
        acorn_put = temp - i[0]

        if(acorn_put >= 0):
            tot += acorn_put // i[2] + 1

    if(tot >= acorn_num):
        max_box = cut
    else:
        min_box = cut

print(max_box)