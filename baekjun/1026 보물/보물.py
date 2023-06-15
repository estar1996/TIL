import sys
sys.stdin = open("input.txt")
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A_lst = sorted(A,reverse=True)
B_lst = sorted(B)
res = 0
for i in range(N):
    res += A_lst[i]*B_lst[i]
print(res)