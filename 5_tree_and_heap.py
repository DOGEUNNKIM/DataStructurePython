
# tree
# parent child 형제  node
# binary tree --> 각 Node 당 자식 Node가 최대 2개
# root node, link == edge , leaf(마지막의 노드), level 0부터 시작
# tree높이, path(path length)

# tree 표현법
# 방법 1 --> list로 저장 --> 1,2,4,8 개수를 지정하여 level별로 저장
# 방법 2 --> list로 저장 --> 자신 노드와 왼쪽, 오른쪽 자식 노드를 한쌍으로 구성
# 방법 3 --> 노드를 직접 정의하여 tree구현


# 방법 1 (Heap)
# 왼쪽 자식노드 H[k] --> H[2*k +1]
# 오른쪽 자식노드 H[k] --> H[2*k +2]
# 부모 노드 H[k] --> H[(k-1)//2]
# 부모, 자식 node 접근은 상수 시간
#
# 모양 성질: 마지막 level 을 빼고 모두 다 차있는 이진트리 
# heap 성질: && 부모 Node key >= 자식 Node key 
# 
# 제공 함수
# insert, find_max (= return H(0))
# delete_max
# make_heap (random의 list를 heap 성질에 맞추어 바꿔주기)


def heapify_down(list_,k,n): 
    #O(log N)
    # index가 작은 값을 자신의 index로 옮기는 것 (내리기)
    while (2*k+1 <= n-1) & (k >= 0):
        left,right = 2*k+1,2*k+2 
        if list_[left] == max(list_[k],list_[left],list_[right]):
            parent_ = list_[k]
            list_[k] = list_[left]
            list_[left] = parent_
            k = (k-1)//2
        elif list_[right] == max(list_[k],list_[left],list_[right]):
            parent_ = list_[k]
            list_[k] = list_[right]
            list_[right] = parent_
            k = (k-1)//2
        else:
            break


def heapify(list_,k,n):
    #O(log N)
    # index가 큰 값을 자신의 index로 옮기는 것 (올리기)
    pass
    

class heap:
    def __init__(self,list_=[]):
        self.list = list_

    def make_heap(self): #nead modify
        #O(N log N)
        n = len(self.list)
        for k in range(n-1,-1,-1):
            heapify_down(self.list,k,n)
    
    def insert(self):
        #O(log N)
        pass #nead modify

    def find_max(self):
        #O(1)
        return self.list[0]

    def delete_max(self):
        pass
        #O(log N)
        # list[0] 지우고 제일 뒤의 값 list[0]로 올린다음 heapify_down하면 됨

aa = heap([1,2,3,4,5,6,7,8,9])
aa.make_heap()
aa.make_heap()

for i in range(9):
    print(aa.list[i])
          