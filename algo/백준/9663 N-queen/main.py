import sys

def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:       # 같은 열에 있거나 대각선에 있다면 False
            return False
    return True
def dfs(x):
    global cnt
    if x == N:                                                      # 끝까지 도착하면 성공 + 1
        cnt += 1
    else:
        for i in range(N):
            row[x] = i
            if check(x):
                dfs(x+1)

N = int(sys.stdin.readline())
row = [0]*N
cnt = 0
# print(row)
dfs(0)
print(cnt)
