import sys
sys.stdin = open('input.txt')



def dfs(n):
    for i in range(C):
        if lst[i][0] == n:
            res.append(lst[i][1])
            return dfs(lst[i][1])

N = int(input())
C = int(input())    # 연결되어 있는 컴퓨터 쌍의 수
lst = []
for _ in range(C):
    l = list(map(int,input().split()))
    lst.append(l)
res = []

dfs(1)
res = set(res)
print(len(res))
