import sys
sys.stdin = open('input.txt')

N,K = map(int,input().split())

dp = [[0] * (K+1) for _ in range(N+1)]

lst = [[0,0]]
for i in range(N):
    w,v = map(int,input().split())
    lst.append([w,v])

for i in range(1,N+1):
    w = lst[i][0]
    v = lst[i][1]

    for j in range(1,K+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
print(dp[N][K])
