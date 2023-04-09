from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num = int(input())
cards = deque([i for i in range(1, num + 1)])
delete = 1

while(cards):
    if(len(cards) > 1):
        if(delete):
            cards.popleft()
            delete = 0
        else:
            cards.append(cards.popleft())
            delete = 1
    else:
        print(cards.popleft())