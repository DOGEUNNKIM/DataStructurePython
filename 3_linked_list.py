# linked list

# index값이 독립적으로 저장되어있음 --> 연결이 되어있음( 자신의 이전 혹은 다음값 위치 저장됨)
# Node ,key(노드의 값), link(노드 사이의 연결)


# 한방향
class Node:
    def __init__(self,key=None):
        self.key = key
        self.next = None
    def __str__(self):
        return str(self.key)
    
a = Node(3)
b = Node(9)
c = Node(15)

a.next = b
b.next = c

class SinglyLinkerdList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size

    ####### insert , delete #######    
    def pushFront(self,key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pushBack(self,key):
        new_node = Node(key)
        if len(self) ==0:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):
        if self.size == 0:
            print ("Size is zero!")
        else:
            x= self.head
            key = x.key
            self.head = x.next
            del x
            self.size -= 1
        return key

    def popBack(self):
        if len(self) ==0:
            print ("Size is zero!")
        else:
            tail = self.head
            while tail.next != None:
                before_tail = tail
                tail = tail.next
            before_tail.next = None
        self.size -= 1
    
    ########## search and generator ######
    def search(self,key):
        object_ = self.head 
        while object_.key != key & object_ != None:
            object_ = object_.next
        if object_ == None:
            return None
        else:
            return object_

    ### for a in L 사용가능
    def __iter__(self):
        v=self.head
        while v != None:
            yield v
            v=v.next

Link = SinglyLinkerdList()
Link.pushBack(1)
Link.pushBack(2)
Link.pushBack(3)
Link.pushBack(4)
Link.pushBack(5)
Link.pushBack(6)
Link.pushFront(0)

for i in Link:
    print(i.key)

print(Link.popFront())
print(Link.popFront())
print(Link.popFront())
print(Link.popFront())
print(Link.popFront())
print(Link.popFront())
print(Link.popFront())
 
# 양뱡향 
# circularly Doublely Linked List
# Doublely Linked List

# splice연산 --> 2개의 노드사이를 잘라서 다른 노드 뒤에 붙여놓기
# 조건 노드 사이에 head노드가 있으면 안됨
# splice 연산을 사용하여 삽입 삭제 이동 연산 가능