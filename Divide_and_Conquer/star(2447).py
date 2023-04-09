import sys
import os

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

def make_stars(leng):
    if(leng == 3):
        base = ["***", "* *", "***"]
        return base
    results = []
    for i in range(3):
        results1 = []
        for j in range(3):
            temp = make_stars(leng // 3)
            if(j == 0):
                results1 = temp
            else:
                if(i == 1 and j == 1):
                    blank = " " * (leng // 3)
                    blanks = [blank for _ in range(len(results))]
                    results1 = [results1[k] + blanks[k] for k in range(len(results1))]
                else:
                    results1 = [results1[k] + temp[k] for k in range(len(results1))]
        if(i == 0):
            results = results1
        else:
            results = results + results1
    return results

length = int(input())

result = make_stars(length)

for i in range(len(result)):
    print(result[i])