import sys
from collections import deque
sys.stdin=open('input.txt')

N, M = map(int,input().split())
r,c,d = map(int,input().split())

arr = []
cnt = 0
for _ in range(N):
    l = list(map(int,input().split()))
    arr.append(l)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(r,c,d):
    global cnt

    if arr[r][c] == 0:          # 이건 최적화 해도 됨
        arr[r][c] = 1
        cnt += 1
        print(r,c)
        for i in range(4):
            nx = dx[(d+i) % 4]
            ny = dy[(d+i) % 4]
            if arr[r+nx][c+ny] == 0:
                dfs(r+nx,c+ny,(d+i) % 4)
    else:
        nx = dx[(d+2) % 4]
        ny = dx[(d+2) % 4]
        if nx > 0 and ny > 0 and nx <= N and ny <= M:
            dfs(nx,ny,(d+2) % 4)
        else:
            return


dfs(r,c,d)
# 문제가 틀리는 이유. 90도 회전 후 앞으로 가면 다른 방향은 안가는 것임을 기억하자.

print(cnt)
# 수정
# 수정중..