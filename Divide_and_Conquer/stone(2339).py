import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def cut_stones(lists, dust, jewel, rc):
    result = 0
    if(len(dust) == 0):
        if(len(jewel) == 1):
            return 1
        else:
            return 0
            
    ind_r = []
    ind_c = []
    for i in dust:
        row = 0
        column = 0
        row_leng = len(lists[0])
        column_leng = len(lists)

        if(rc!= "r"):
            for j in lists[i[0]]:
                if(j == 2):
                    break
                else:
                    row += 1

        if(rc != "c"):
            for j in range(column_leng):
                if(lists[j][i[1]] == 2):
                    break
                else:
                    column += 1

        temp = dust[:]
        tempj = jewel[:]
        if(row == row_leng and (i[0] not in ind_r)):
            if(i[0] != 0 and i[0] < column_leng - 1):
                result1 = 0
                result2 = 0
                list1 = lists[: i[0]]
                list2 = lists[i[0] + 1 :]
                temp1 = []
                temp2 = []
                tempj1 = []
                tempj2 = []

                for j in temp:
                    if(j[0] < i[0]):
                        temp1.append(j)
                    if(j[0] > i[0]):
                        temp2.append(j)

                for j in tempj:
                    if(j[0] < i[0]):
                        tempj1.append(j)
                    if(j[0] > i[0]):
                        tempj2.append(j)

                temp2 = [[temp2[j][0] - i[0] - 1, temp2[j][1]] for j in range(len(temp2))]
                tempj2 = [[tempj2[j][0] - i[0] - 1, tempj2[j][1]] for j in range(len(tempj2))]
                result1 = cut_stones(list1, temp1, tempj1, "r")
                result2 = cut_stones(list2, temp2, tempj2, "r")
                result += result1 * result2

                if(result > 0):
                    if(rc != "rc"):
                        for j in temp:
                            if (j[0] == i[0]):
                                temp.remove(j)
                    else:
                        ind_r.append(i[0])

        if(column == column_leng and (i[1] not in ind_c)):
            if(i[1] != 0 and i[1] < row_leng - 1):
                result1 = 0
                result2 = 0
                list1 = [lists[j][: i[1]] for j in range(column_leng)]
                list2 = [lists[j][i[1] + 1 :] for j in range(column_leng)]

                temp1 = []
                temp2 = []
                tempj1 = []
                tempj2 = []

                for j in temp:
                    if(j[1] < i[1]):
                        temp1.append(j)
                    if(j[1] > i[1]):
                        temp2.append(j)

                for j in jewel:
                    if(j[1] < i[1]):
                        tempj1.append(j)
                    if(j[1] > i[1]):
                        tempj2.append(j)

                temp2 = [[temp2[j][0], temp2[j][1] - i[1] - 1] for j in range(len(temp2))]
                tempj2 = [[tempj2[j][0], tempj2[j][1] - i[1] - 1] for j in range(len(tempj2))]
                result1 = cut_stones(list1, temp1, tempj1, "c")
                result2 = cut_stones(list2, temp2, tempj2, "c")
                result += result1 * result2
                if(result > 0):
                    if(rc != "rc"):
                        for j in temp:
                            if (j[1] == i[1]):
                                temp.remove(j)
                    else:
                        ind_c.append(i[1])
    return result

length = int(input())

stones = [list(map(int,input().split())) for _ in range(length)]

dusts = []
jewels = []

for i in range(length):
    for j in range(length):
        if(stones[i][j] == 1):
            dusts.append([i, j])
        elif(stones[i][j] == 2):
            jewels.append([i, j])

result = cut_stones(stones, dusts, jewels, "rc")

if(result == 0):
    result = -1

print(result)