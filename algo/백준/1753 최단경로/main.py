import sys
sys.stdin = open('input.txt')

V, E = map(int,input().split())
K = int(input())
graph = [[] for i in range(V + 1)]
INF = int(1e9)
distance = [INF] * (V + 1)
visited = [False] * (V + 1)
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

def get_smallest_node():
    min_value = INF
    index = 0   # 가장 최단 거리가 짧은 노드 (인덱스 )
    for i in range(1,V + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dikjstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for k in range(V - 1):
        now = get_smallest_node()
        visited[now] = True
        for l in graph[now]:
            cost = distance[now] + l[1]
            if cost < distance[l[0]]:
                distance[l[0]] = cost
dikjstra(K)
for i in range(1,V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
print(graph)