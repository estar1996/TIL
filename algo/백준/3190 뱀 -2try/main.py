
from collections import deque
import sys
# sys.stdin = open('input.txt')

N = int(input())                    # 보드 크기
K = int(input())                    # 사과의 개수

arr = [[0] * (N) for _ in range(N)]

for _ in range(K):
    x,y = map(int,input().split())
    arr[x][y] = 2

L = int(input())
lst = []
for _ in range(L):
    s,d = map(str,input().split())
    s = int(s)
    lst.append([s,d])

c = (1,1)
snake = deque()
sec = 0
snake_l = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
nx, ny = 0, 0
tmp = 0
Q = deque()
i = 0                           # 방향 전환할 때마다 + 1
while 1:
    sec += 1
    nx += dx[tmp]
    ny += dy[tmp]
    if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in Q:         # 종료 조건 ( 벗어나거나, 자기 자신의 몸에 부딪히거나)
        break
    Q.append((nx,ny))
    if arr[nx][ny] == 0:
        Q.popleft()
    else:
        arr[nx][ny] = 0                 # 사과가 있으면 먹은거니까 ... 대신 pop 안함으로 몸 길이는 Q에 저장
    if sec == lst[i][0]:
        if lst[i][1] == 'D':
            tmp = (tmp + 1) % 4
        else:
            tmp = (tmp - 1) % 4

        if i+1 < L:
            i += 1
print(sec)



