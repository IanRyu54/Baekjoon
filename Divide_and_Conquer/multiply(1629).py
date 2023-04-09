import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

def mult(a, b, c):
    if(b == 1):
        return a % c
    elif(b % 2 == 0):
        return (mult(a, divmod(b, 2)[0], c) ** 2) % c
    else:
        return (mult(a, divmod(b, 2)[0], c) ** 2 * a) % c

A, B, C = map(int, input().split())

print(mult(A, B, C))