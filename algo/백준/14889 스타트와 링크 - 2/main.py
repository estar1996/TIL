import sys
sys.stdin = open("input.txt")

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
lst = []


for i in range(N):
    for j in range(N):
