from hashlib import new
import sys
sys.stdin = open("input.txt")

N, K = map(int,input().split())
lst = []
for _ in range(1,N+1):
    
    WV = list(map(int,input().split()))
    
    lst.append(WV)


for _ in range(N):
    temp = 0
    temp_w = 0
    for i in range(N):
        if temp + lst[i+1][0] < K :

