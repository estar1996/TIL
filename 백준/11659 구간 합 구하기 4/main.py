import sys
sys.stdin = open('input.txt')
N,M = map(int,input().split())
lst = list(map(int,input().split()))
res = [0]*(N+1)

for k in range(N):
    res[k+1] = res[k] + lst[k]


for _ in range(M):
    i,j =map(int,input().split())
    print(res[j] - res[i-1])