import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

size, number = map(int, input().split())
queues = [i for i in range(1, size + 1)]

ind = 0
print("<", end = "")

for i in range(size):
    ind = (ind + number - 1) % len(queues)
    print(queues[ind], end = "")
    del queues[ind]

    if(i != size - 1):
        print(", ", end = "")
    else:
        print(">", end = "")