import sys
sys.stdin = open('input.txt')
N,K = map(int,input().split())


lst = []
for _ in range(N):
    wv = list(map(int,input().split()))
    lst.append(wv)

print(lst)