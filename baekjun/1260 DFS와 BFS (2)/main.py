import sys
sys.stdin = open('input.txt')

def dfs(n):
    return n


N,M,V = map(int,input().split())

arr = []
for _ in range(M):
    lst = list(map(int,input().split()))
    arr.append(lst)
