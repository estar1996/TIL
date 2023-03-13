import sys
sys.stdin = open('input.txt')

F,S,G,U,D = map(int,input().split())
D = -D

lst = []


visited = [0] * (F + 1)

def dfs(n):
    global res, tmp
    res += 1

    if tmp + n <= F and visited[tmp + n] == 0:
        tmp += n
        visited[tmp] = 1
    else:
        return
    if tmp == G:
        lst.append(res)
        return
    else:
        if S + U <= F and visited[S + U] == 0:
            dfs(U)
        if S + D >= 1 and visited[S + D] == 0:
            dfs(D)

for i in range(2):
    tmp = S
    res = 0
    if i == 0:
        dfs(U)
    else:
        dfs(D)


if lst:
    print(min(lst))
else:
    print('use the stairs')