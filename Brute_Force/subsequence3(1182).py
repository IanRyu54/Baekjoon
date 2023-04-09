import sys

sys.stdin = open('input.txt', 'r')

def make_comb(arr, comb, s):
    cnt = 0
    for front in arr:
        print(front)
        print(comb)
        for end in list(comb):
            comb.append(front + end)
            if comb[-1] == s:
                cnt += 1
            print(comb)
        print()
    return cnt

n, s = map(int, input().split())
comb = [0]
cnt = make_comb([*map(int, input().split())], comb, s)
print(cnt)