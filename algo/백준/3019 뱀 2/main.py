import sys
sys.stdin = open('input.txt')

dx = [0,1,0,-1]
dy = [1,0,-1,0]



N = int(input())
K = int(input())

arr = [[0]*N for _ in range(N)]
apple = []
snake = 1               # 뱀
snake_l = 1             # 뱀 길이...
cnt = 1
for _ in range(K):
    x,y = map(int,input().split())
    arr[x-1][y-1] = -1
    apple.append((x,y))
arr[0][0] = snake
L = int(input())
L_lst = []
for _ in range(L):
    l = list(map(str,input().split()))
    l[0] = int(l[0])
    L_lst.append(l)
print(arr)

d = 100                   # 방향
for x in range(10):
    tmp = 1             # 몇번째 시도인지

    nx = dx[(d % 4)]
    ny = dy[(d % 4)]
    for x in range(len(L_lst)):
        if tmp == L_lst[x][0]:
            if L_lst[x][1] == 'D':
                d += 1
            elif L_lst[x][1] == 'L':
                d -= 1
    # 좌표를 스택에 저장해놓는거로 하면 좋을듯
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                if 0 < (i + nx) < N and 0 < (i + ny) < N:
                    if arr[i + nx][j + ny] == 0:
                        arr[i + nx][j + ny] = 1
                        arr[i + nx - snake_l][j + ny - snake_l] = 0
                    elif arr[i + nx][j + ny] == -1:
                        arr[i + nx][j + ny] = 100
                        snake_l += 1



print(arr)