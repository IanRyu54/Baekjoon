import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

init_str = input().split("\n")[0]
order_num = int(input())
orders = [list((input().split("\n")[0]).split()) for _ in range(order_num)]

class Node:
    def __init__(self, value, next, prev) -> None:
        self.value = value
        self.prev = prev
        self.next = next

class LList:
    def __init__(self) -> None:
        self.leng = 0
        self.head = Node(None, None, None)
        self.origin = self.head
        self.curr = None

    def __iter__(self):
        self.curr = self.origin.prev
        return self
    
    def __next__(self):
        if self.curr is None:
            raise StopIteration
        else:
            temp_val = self.curr.value
            self.curr = self.curr.prev
            return temp_val
    
    def __len__(self):
        return self.leng

    def move_left(self):
        if(self.head.next != None):
            self.head = self.head.next
    
    def move_right(self):
        if(self.head.prev != None):
            self.head = self.head.prev
    
    def back_space(self):
        if(self.head.next != None):
            self.head.next.prev = self.head.prev
            if(self.head.prev != None):
                self.head.prev.next = self.head.next
            self.head = self.head.next
        self.leng -= 1
    
    def insert_left(self, val):
        self.head = Node(val, self.head, self.head.prev)
        if(self.head.next != None):
            self.head.next.prev = self.head
        else:
            self.origin = self.head

        if(self.head.prev != None):
            self.head.prev.next = self.head
        self.leng += 1
    
    def print_all(self, enter = False):
        self.curr = self.origin.prev
        while(self.curr != None):
            temp = self.curr.value
            print(temp, end = "")
            self.curr = self.curr.prev
        if(enter == True):
            print()
    

istr = LList()
for i in init_str:
    istr.insert_left(i)

for i in orders:
    if(i[0] == "L"):
        istr.move_left()
    elif(i[0] == "D"):
        istr.move_right()
    elif(i[0] == "B"):
        istr.back_space()
    else:
        istr.insert_left(i[1])

istr.print_all(True)