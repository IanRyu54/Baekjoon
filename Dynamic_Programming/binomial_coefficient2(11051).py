import sys
from fractions import Fraction

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

natural, integer = map(int, input().split())

result = Fraction(1, 1)

for i in range(integer):
    result *= Fraction(natural - i, i + 1)

print(result % 10007)