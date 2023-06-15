import sys
from collections import deque
sys.stdin = open("input.txt")
N,K = map(int,input().split())
dp = [[0]*(K+1) for _ in range(N)]

lst = []
for i in range(N):
    w,v = map(int,input().split())
    lst.append((w,v))
for j in range(N):
    w1,v1 = lst[j]
    for k in range(1,K+1):
        if k < w1:
            dp[j][k] = dp[j-1][k]
        else:
            dp[j][k] = max(dp[j-1][k-w]+v1,dp[j-1][k])
print(dp)