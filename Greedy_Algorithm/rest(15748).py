import sys

sys.stdin = open('input.txt', 'r')

if __name__ == '__main__':
    tot_length, tot_stops, farmer, bessie = map(int,input().split())
    tasty = [tuple(map(int,input().split())) for _ in range(tot_stops)]

    tasty.sort(key = lambda x : x[1], reverse = True)

    speed_diff = farmer - bessie

    now_loc = 0
    result = 0

    for i in tasty:
        if(i[0] > now_loc):
            result += (i[0] - now_loc) * i[1] * speed_diff
            now_loc = i[0]

    print(result)