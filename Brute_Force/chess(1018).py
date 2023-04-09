import copy
import sys

sys.stdin = open('input.txt', 'r')

num1, num2 = map(int,input().split())
original = [input() for _ in range(num1)]

board1 = []

for i in range(4):
    board1.append("BWBWBWBW")
    board1.append("WBWBWBWB")

score = 64

for i in range(num1-7):
    for j in range(num2-7):
        score1 = 0
        temp_ori = []
        for k in range(8):
            temp_ori.append(original[i+k][j:j+8])
        
        for k in range(8):
            for l in range(8):
                if(temp_ori[k][l] == board1[k][l]):
                    score1 = score1 + 1

        temp = min(score1,64-score1)
        if(temp < score):
            score = temp

print(score)