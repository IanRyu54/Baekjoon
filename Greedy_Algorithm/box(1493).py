import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

length, width, height = map(int,input().split())
num_cube = int(input())
cubes = [list(map(int, input().split())) for _ in range(num_cube)]

tot_vol = length * width * height

cubes.sort(reverse = True)

result = 0

length_div = []
width_div = []
height_div = []

templ = length
tempw = width
temph = height
temp = 1

for side, numb in cubes:
    side_len = 2 ** side
    quol, reml = divmod(templ, side_len)
    quow, remw = divmod(tempw, side_len)
    quoh, remh = divmod(temph, side_len)
    quorl, remrl = divmod(length, side_len)
    quorw, remrw = divmod(width, side_len)
    quorh, remrh = divmod(height, side_len)

    length_div.append(quol)
    templ = reml
    width_div.append(quow)
    tempw = remw
    height_div.append(quoh)
    temph = remh
    
    box_need = quol * quorw * quorh + quow * quorh * quorl + quoh * quorl * quorw - quol * quow * quorh - quow * quoh * quorl - quoh * quol * quorw + quol * quow * quoh

    if(box_need > numb):
        if(side > 0):
            result += numb
            left_vol = (box_need - numb) * (side_len ** 3)
            for j in range(temp, len(cubes)):
                temp_side = 2 ** cubes[j][0]
                new_vol = temp_side ** 3
                if(cubes[j][1] * new_vol >= left_vol):
                    cubes[j][1] -= divmod(left_vol, new_vol)[0]
                    result += divmod(left_vol, new_vol)[0]
                    break
                else:
                    if(cubes[j][0] == 0):
                        cubes[j][1] = 0
                        result = -1
                    else:
                        left_vol -= cubes[j][1] * new_vol
                        result += cubes[j][1]
                        cubes[j][1] = 0
        else:
            result = -1
    else:
        result += box_need

    
    if(templ + tempw + temph == 0):
        break

    temp += 1

print(result)