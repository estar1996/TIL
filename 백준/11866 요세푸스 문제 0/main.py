import sys
# sys.stdin = open('input.txt')

N,K = map(int,input().split())
lst = []
for i in range(1,N+1):
    lst.append(i)
res = []
idx = 0
while lst:
    idx += K -1
    if idx >= len(lst):
        idx %= len(lst)
    deleted = lst[idx]
    lst.remove(lst[idx])
    res.append(deleted)
print("<" + ", ".join(map(str,res)) + ">")
# 출력 방식 기억하기...