import sys
sys.stdin= open("sample_input(3).txt")
from collections import deque

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E):
        s, e = map(int, input().split())
        lst[s].append(e)
        lst[e].append(s)
    S, G = map(int, input().split())

    N_q = deque()
    N_q.append(S)                           # 새로운 큐에 시작점을 추가한다.


    while N_q :
        value = N_q.pop()
        for i in lst[value]:
            if visited[i] == 0 :
                N_q.append(i)
                visited[i] = visited[value] +1
    if visited[G] != 0:
        res = visited[G]
    else :
        res = 0
    
    
    print("#{} {}".format(tc,res))
















 
# T = int(input())
# for t in range(1, T+1):
#     V, E = map(int, input().split())
#     lst = [[] for _ in range(V+1)]
#     visited = [0]*(V+1)
#     for _ in range(E):
#         s, e = map(int, input().split())
#         lst[s].append(e)
#         lst[e].append(s)
#     S, G = map(int, input().split())

#     q = deque()
#     q.append(S)
#     visited[S] = 1
#     print(visited)
#     print(lst)
#     print(q)
    
#     while q:
#         value = q.popleft()
#         for node in lst[value]:
#             if not visited[node]:
#                 q.append(node)
#                 visited[node] = visited[value]+1
#         print(visited)
