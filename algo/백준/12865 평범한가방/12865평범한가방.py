from hashlib import new
import sys
sys.stdin = open("input.txt")

N, K = map(int,input().split())
lst = []
for _ in range(1,N+1):
    
    WV = list(map(int,input().split()))
    
    lst.append(WV)

for i in range(len(lst)):
    lst[i].append(lst[i][1]/lst[i][0])

lst.sort(key = lambda x:-x[2])
print(lst)
W_lst = []


for k in range(len(lst)):
    cnt = 0
    if K // lst[k] > 0:
        cnt += K // lst[k]
        K = K // lst[k]




    # for j in range(len(lst)):
    #     K_1 = K
    #     cnt = 0
    #     cnt += ( K_1 // lst[j][0] ) * lst[j][1]
    #     K_1 = K_1 % lst[j][0]
    #     W_lst.append(cnt)
print(K)
print(W_lst)