import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

length = int(input())
sequence = list(map(int,input().split()))

max_seq = sequence[:]

for i in range(len(sequence)):
    for j in range(i):
        if(sequence[j] < sequence[i]):
            max_seq[i] = max(max_seq[i], sequence[i] + max_seq[j])

print(max(max_seq))