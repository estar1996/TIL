import sys
sys.stdin = open('input.txt')

def prim1(r,V):
    MST = [0]*(E)
    key = [float('inf')]*(V+1)
    key[r] = 0
    for _ in range(V+1):
        u = 0
        minV = float('inf')
        for i in range(V+1):
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        MST[u] = 1

        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v]>0:

                key[v] = min(key[v], adjM[u][v])
    return sum(key)


T = int(input())

for tc in range(1,T+1):
    V, E = map(int,input().split())
    adjM = [[0]*(E) for _ in range(V+1)]
    adjL = [[] for _ in range(V+1)]

    for _ in range(E):
        u,v,w = map(int,input().split())
        adjM[u][v] = w
        adjM[v][u] = w
    # res = []
    print(prim1(0,V))
    # print(adjM)
