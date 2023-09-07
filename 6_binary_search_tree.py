# heap 은 search 불가능 & list memory공간 낭비 존재
# tree 표현법3
# 꽉 차있지 않은 이진 tree

class Node():
    def __init__(self,key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)

    def preorder(self):
        if self != None:
            print(self.key)
            if self.left != None:
                self.left.preorder()
            if self.right != None:
                self.right.preorder()
    
    def inorder(self):
        if self != None:
            if self.left != None:
                self.left.inorder()
            print(self.key)
            if self.right != None:
                self.right.inorder()

    def postorder(self):
        if self != None:
            if self.left != None:
                self.left.postorder()
            if self.right != None:
                self.right.postorder()
            print(self) #__str__함수로 인해 가능
            

# binary tree 만들기 
a = Node(6)
b = Node(9)
c = Node(1)
d = Node(5)

a.left = b
a.right =c
b.parent =a 
c.parent = a
b.left = d
d.parent =b 

# tranversal(순회) 
# --> preorder: 나 먼저 Me Left Right
# --> inorder: 나 가운데 Left Me Right
# --> postorder: 나 뒤에 Left Right Me
a.inorder()
a.preorder()
a.postorder()

# reconstruct(재구조)
# preorder, inorder, postorder 을 보고 이진트리 재구성하기


# Binary Search Tree(BST)
# condition: right key value > left key value
#  --> search하기 위한 조건

class BST:
    def __init__(self):
        self.root =None
        self.size =0
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def find_loc(self,key):
        if self.size ==0:
            return None
        p = None
        v = self.root
        while v != None:
            if v.key == key:
                return v,p
            elif v.key < key:
                p = v
                v = v.right
            else:
                p=v
                v = v.left
        return v, p
    
    def search(self,key):
        v, _ = self.find_loc(key)
        if v == None:
            return None
        else:
            return v

    def insert(self,key):
        v,p = self.find_loc(key)
        if p == None or p.key!=key:
            node = Node(key)
            if p == None:
                self.root = node
            else:
                node.parent =p
                if p.key >= key:
                    p.left = node
                else:
                    p.right = node
            self.size +=1
            return node
        else:
            print("already exist!")
    

    def delete(self,x):
        pass
        #delete by copy
        #delete by merge





            



tree = BST()
tree.root = a

