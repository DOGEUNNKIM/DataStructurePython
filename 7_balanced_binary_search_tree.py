# Balanced BST
# tree height max는 log(n+1)이상 n-1이하를 가짐
# -->검색시간인 O(h)를 log(n) 로 맞추는 tree
#
# 종류 --> AVL, Red-Black, 2-3-4 tree
# 방법: 기준을 두고 검색시간이 늘어나면 tree를 rotation시켜서 재구성함 
#       -->height가 줄어들음 --> 검색시간이 줄어들음


# AVL tree
#
# 모든 노드의 오른쪽 왼쪽 sub_tree의 height 차이가 1이하인 tree
# --> 검색시간이 log(n)이 됨
#
# 검색 O(logN) 증명
# h_level의 필요 최소 노드 갯수 관계식: N(h+2) = 1 + N(h+1) + N(h)
# --> n > N(h) > 2^(h/2)
# --> h < log2(n)

# Red-Black tree
#
# None node들이 마지막에 모두 존재 = leaf node
# key가 있는 node = 내부 node
# 조건:
# 1. 모든 노드 red 혹은 black
# 2. root는 black
# 3. leaf는 black
# 4. red의 child는 black
# 5. 특정 node에서 leaf로 가는 동안 black node갯수 동일
#
# 검색 O(logN) 증명
# bh(v): v-> leaf로 갈때 black node 갯수, h(v): v의 height
# 사실1: v의 sub_tree 내부 노드 갯수 > 2^bh(v) -1 : 귀납적으로 증명 가능
# 사실2: bh(root) >= h/2
# --> 사실 1,2에 의해 h < 2log2(n) 
# --> 2-3-4 tree에서 모두 3node라면 red black tree의 height < 2log3(N)임을 증명 가능

# 2-3-4 tree
#
# binary tree 아님
# node당 key값 3개
# child node 갯수 2,3,4
# leaf node는 같은 level에 존재
# log4(n) < h < log2(n)
# insert는 leaf에만 가능 & 이미 leaf가 차있을때 4node를 split시키면서 내려감(가운테 key값을 부모노드로 옮김)
# 2-3-4 tree와 red-black tree는 서로 변경가능
# 2 node = 1 level, 3,4 node = 2 level --> red black tree 조건을 만족시키게 됨
