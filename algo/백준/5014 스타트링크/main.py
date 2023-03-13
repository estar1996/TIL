import sys
sys.stdin = open('input.txt')

f,s,g,u,d = map(int,input().split())
d = -d
cnt = 0
res = []

def dfs(c,num):
    global cnt
    c += num
    cnt += 1
    if c > g:
        res.append(cnt)
        return 0
    elif c < 1:
        return 0
    elif c > f:
        return 0
    dfs(c,u)
    dfs(c,d)
    return 0


