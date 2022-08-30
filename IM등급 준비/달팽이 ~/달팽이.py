n = 5
snail = [[0]*n for _ in range(n)]

num = 1                                 # 0 부터 시작해도 됨
    # 우  하  좌  상
    # 0   1   2   3
dx = [0,1,0,-1]
dy = [1,0,-1,0]

x,y = 0,-1                               # 시작점
# 하나 전에서 시작해야 1부터 칠한다. 0,0 으로 할 경우 숫자를 넣고 이동하는 로직을 구혀하면 된다.
d = 0
while num <= n**2:                                # 언제 멈출지 모르니까
    # 이동
    # 숫자 넣기
    nx = x + dx[d]
    ny = y + dy[d]
    # 숫자 넣기

    if 0 <= nx < n and 0 <= ny < n and snail[nx][ny] == 0:
        #숫자 넣기
        snail[nx][ny] = num
        x = nx
        y = ny
        num += 1
    else :
        d = (d+1)%4

print(snail)