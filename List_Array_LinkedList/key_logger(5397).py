import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num_case = int(input())
cases = [input().split("\n")[0] for _ in range(num_case)]

for i in cases:
    left_words = []
    right_words = []
    
    for j in i:
        if(j == "<"):
            if(left_words):
                right_words.append(left_words.pop())
        elif(j == ">"):
            if(right_words):
                left_words.append(right_words.pop())
        elif(j == "-"):
            if(left_words):
                left_words.pop()
        else:
            left_words.append(j)

    print("".join(left_words + right_words[::-1]))