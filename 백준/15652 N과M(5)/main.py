import sys
N,M = map(int,input().split())
res_lst = []
def f(start):
    if len(res_lst) == M:
        print(' '.join(map(str,res_lst)))
        return
    for i in range(start,N+1):
        res_lst.append(i)
        f(i)
        res_lst.pop()


f(1)
