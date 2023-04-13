import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

tot_num, nums = map(int, input().split())
tot_real = tot_num + 1
tot_list = []

def numbering(tmp_list, visited, depth):
    if(depth > 1):
        for i in range(1, tot_real):
            if(not visited[i]):
                tmp_list.append(i)
                visited[i] = 1
                numbering(tmp_list, visited, depth - 1)
                tmp_list.pop()
                visited[i] = 0
    else:
        tot_list.append(' '.join(list(map(str, tmp_list))))

for i in range(1, tot_real):
    temp = []
    visiting = [0 for _ in range(tot_real)]
    temp.append(i)
    visiting[i] = 1
    numbering(temp, visiting, nums)

print('\n'.join(tot_list))