import sys
import copy

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

num_people, bus_people = map(int, input().split())
wanted = list(map(int, input().split()))
visited = [0 for _ in range(num_people)]
finished = [0 for _ in range(num_people)]

def take_bus(ind):
    global cur_cycle
    global temp_size
    visited[ind] = 1
    arrow = wanted[ind] - 1
    if(not visited[arrow]):
        take_bus(arrow)
    else:
        while(not finished[arrow]):
            cur_cycle += 1
            finished[arrow] = 1
            ind = arrow
            arrow = wanted[ind] - 1
            temp.append(ind)

def find_size(ind):
    global size_ind
    temp = size_ind[:]
    for i in range(1001):
        if(size_ind[i] == 1):
            for j in range(sizes[ind][0], sizes[ind][1] + 1):
                if(j + i < 1001):
                    temp[j + i] = 1
    size_ind = temp[:]
    return

cycles = []
result = 0

for i in range(num_people):
    cur_cycle = 0
    temp = []
    comp = []
    if(not visited[i]):
        take_bus(i)
        if(temp):
            cycles.append(temp)
    finished[i] = 1

components = copy.deepcopy(cycles)
in_cycle = [0 for _ in range(num_people + 1)]

leng = 0
for i in components:
    leng += len(i)
while(leng < num_people):
    for i in range(num_people):
        for j in range(len(components)):
            if(wanted[i] - 1 in components[j] and i not in components[j]):
                components[j].append(i)
                leng += 1

sizes = []
for i in range(len(components)):
    sizes.append([len(cycles[i]), len(components[i])])

sizes.sort()
for i in range(len(sizes) - 1, -1, -1):
    if(sizes[i][0] > bus_people):
        sizes.pop()
        
size_ind = [0 for _ in range(1001)]
size_ind[0] = 1
for i in range(len(sizes)):
    find_size(i)

for i in range(bus_people + 1):
    if(size_ind[i]):
        result = i

print(result)