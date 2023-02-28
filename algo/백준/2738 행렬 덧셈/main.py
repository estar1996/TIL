import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())

arr1 = []
arr2 = []
res = []
for _ in range(N):
    l = list(map(int,input().split()))
    arr1.append(l)
for _ in range(N):
    ll = list(map(int,input().split()))
    arr2.append(ll)
for i in range(N):
    for j in range(M):
        res.append(arr1[i][j] + arr2[i][j])

for x in range(len(res)):
    if (x+1) % 3 != 0:
        print(res[x],end=' ')
    else:
        print(res[x])
        # print()


