import sys

input = sys.stdin.readline

texts = []
temp = ""

temp = input().split("\n")[0]

while(True):
    texts.append(temp)
    temp = input().split("\n")[0]
    if(temp == "#"):
        break

for i in texts:
    ind = 0
    open_tag = 0
    save_name = 0
    temp_list = []
    temp = ""
    while(ind < len(i)):
        if(i[ind] == "<"):
            if(i[ind + 1] == "/"):
                save_name = 2
            else:
                save_name = 1
        elif(i[ind] == ">"):
            if(i[ind - 1] != "/"):
                if(save_name == 3):
                    if(not temp_list):
                        temp_list.append(i)
                        break
                    if(temp_list.pop() != temp):
                        break
                    temp = ""
                if(temp):
                    temp_list.append(temp)
                temp = ""
                save_name = 0
            else:
                temp = ""
                save_name = 0
        elif(i[ind] == " " and save_name == 1):
            if(i[ind + 1] != "/" and i[ind - 1] != "/"):
                if(save_name == 3):
                    if(temp_list.pop() != temp):
                        break
                    temp = ""
                if(temp):
                    temp_list.append(temp)
                temp = ""
                save_name = 0
            else:
                temp = ""
                save_name = 0
        else:
            if(save_name == 1 or save_name == 3):
                temp += i[ind]
            elif(save_name == 2):
                save_name = 3
        
        ind += 1
        
    if(len(temp_list)):
        print("illegal")
    else:
        print("legal")