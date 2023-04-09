import sys

sys.stdin = open('wordle.txt', 'r')

words = [input().strip("\n") for _ in range(16962)]
dicts = {}

sys.stdin = open('wordle1.txt', 'r')
nums = int(input())
wordle = [input().strip("\n").split() for _ in range(nums)]
temp = []

for w in wordle:
    print(w)
    for i in words:
        ind = 0
        truth = 1
        for j in i:
            iscore = int(w[1][ind])
            if(iscore == 0):
                if(w[0][ind] in i):
                    truth = 0
                    break
            elif(iscore == 1):
                if(w[0][ind] not in i):
                    truth = 0
                    break
                if(w[0][ind] == j):
                    truth = 0
                    break
            else:
                if(j != w[0][ind]):
                    truth = 0
                    break
            ind += 1

        if(truth == 1):
            temp.append(i)
    words = temp[:]
    temp = []

    print(words)