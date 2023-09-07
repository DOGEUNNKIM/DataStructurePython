# Graph
# 
# Graph = vertex(node) + edge
# vertex is construct of Id
# edge is constructed of pair of vertex
# edge is representing relation of nodes
# edge = undirected, directied
# 
# example of graph = 지하철 노선도
# 
# degree: node와 연결된 node 갯수
# 인접하다: edge로 연결되어있다.
# path
# cycle: 닫힌 path --> tree는 cycle 없음
# cycle가 없다 == 경로가 1개만 있다
# 
# 표현법 : 행렬로 표현, linked list로 표현
# 
# 행렬표현법: memory 낭비가 심함 
# memory = O(n^2)
# (u,v) 존재? = O(1)
# edge 삽입 : 행렬 값 1개 변경
# 
# linked list 표현법: 자기 자신과 edge로 연결된 node들을 linked list로 저장
# memory = O(n+m)  edge갯수:m, node갯수:n
# (u,v) 존재? = O(n)
# 노드 1개에 인접한 갯수만 접근할때는 linked list가 이득
# edge 삽입 : pushfront하기
# Sparse graph에 대해서 이득임
# 
# Graph Traversal - DFS(깊이 우선 탐색), BFS(너비 우선 탐색) 
# DFS : 자신으로부터 시작하여 안가본 곳 선택 후 갈 곳이 없으면 뒤로 돌아감
# --> 먼저 접근한 것을 parent로 저장하여 새로운 tree를 만들 수 있음
# --> DFS Tree
# --> level 개념 등장
#
# Search
# 모든 노드에 대해서 DFS Traversal을 하면 알 수 있음
#
# 비제귀적 Graph Traversal 구현
# stack 사용함

"""
DFS Traversal
pseudo code

stack.push((None,S))
while stack is not empty:
    p,v = stack.pop()
    if v is unmarked:
        mark[v] = "visited"
        parent[v] = p
        for each edge(v,w):
            if w is unmarked:
                stack.push((v,w))

"""

# back edge: DFS tree에서 사용 하지 않은 edge
# --> back edge가 존재한다면 cycle 존재함

# DAG (Directed Acyclic Graph)
# 사이클이 없는 방향 그래프
# --> 위상정렬 : 일의 조건이 있어서 순서를 지켜서 전부 순회하는 정렬
# DFS의 Traversal에 맞추어 비교하면 post time이 느린 순서대로 정렬하면 위상정렬과 동일해짐

