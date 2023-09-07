# Shortest path
# Source -> Dest
# a-->b 최단 경로가 있다면 사이 노드 C로 가는 최단 경로는 a-->b 경로임
# 최단 경로 = min(이전 노드까지의 경로 + 노드 weight) 
# 
# one to all
#
# Bellman Ford algorithm
# relax: 최단경로를 비교하면 update하는 과정
# node 갯수가 n개라면 경로 사이에 node는 많아봤자 n-2개임 
# --> n-1번의 update를 하면 최적의 경로 나옴
"""
Bellman Ford algorithm
pseudo code
O(n*E) = O(n^3) # 너무 느림

for i in range(n-1):
    for each edge(u,v) in Graph:
        if dist[v] > dist[u] + w(u,v):
            dist[v] = dist[u] + w(u,v)   #relax(u,v)
"""
# Dijkstra algorithm
# Bellman Ford algorithm의 속도 향상시킨 알고리즘
# relax할 때 dist가 가장 작은 값을 가진 node만 relax시킴
# parent 랑 child를 연결하면 최단경로 tree가 만들어짐
"""
Dijkstra algorithm
pseudo code
N^2*log(N)

Q = min_heap with dist[v] as key # O(N*log(N) 
while Q != None:
    u= Q.deleteMin()
    for each u -> v:
        relax (u,v)
        Q.decreaseKey(v,dist[v])  # O(logN) #heapify_up
"""

# all to all
# 방법1: 모든 노드에 대해 Dijkstra algorithm 호출하기 O(N^3*log(N))
# 방법2: Dynamic Programing사용 --> Floyd-warshall algorithm

# Floyd-warshall algorithm
# node 1~n중 i~j의 최단경로를 구해야함
# ShortestPath(n)(3,8): node3에서 node8로 가는데 경로중에 최대값이 nodeN인 경로
# distance사이의 점화식은 ShortestPath를 distance로 바꾸어서 구현 가능
# distance사이의 점화식을 구해서 all to all dist를 다 계산 가능
# --> O(n^3)으로 줄일 수 있음

"""
Floyd-warshall algorithm
pseudo code
N^3

dist_list = list(N,N) : init = inf
for k = 1:n:
    for all (i,j):
        dist_list[i][j] = min(dist_list[i][j], dist_list[i][k]+ dist_list[k][j])
"""



