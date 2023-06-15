adjList = [
    [1,2],              # 0
    [0,3,4],            # 1
    [0,4],              # 2
    [1,5],              # 3
    [1,2,5],            # 4
    [3,4,6],            # 5
    [5]                 # 6
]

def dfs(v,N):
    top = -1


    visited[v] = 1      # 시작점 방문 표시
    while True:
        for w in adjList[v]:        # if ( v 의 인접 정점 중 방문 안한 정점 w가 있으면 )
            if visited[w] == 0:     # push(v)
                top += 1
                stack[top] = v
                # v <- w ( w 에 방문 )
                v = w
                visited[w] = 1
                break
            else:                   # w 가 없으면
                if top != -1:       # 스택이 비어있지 않은 겨웅
                    v = stack[top]  # pop
                    top -= 1
                else:               # 스택이 비어있으면
                    break

N = 7
visited = [0] * N   # visited 생성
stack = [0] * N     # stack 생성
dfs(1,N)
