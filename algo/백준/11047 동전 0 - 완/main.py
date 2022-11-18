import sys
sys.stdin = open("input.txt")

N,K = map(int,input().split())

V_lst = []
for _ in range(1,N+1):
    A = int(input())
    V_lst.append(A)


cnt = 0
for i in range(1,len(V_lst)+1):
    cnt += (K//V_lst[-i])
    K = K -(K//V_lst[-i])*V_lst[-i]

print(cnt)
