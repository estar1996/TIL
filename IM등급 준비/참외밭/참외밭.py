import sys
sys.stdin = open("input.txt")

K = int(input())

C_lst = []
for _ in range(6):
    D , L = map(int,input().split())
    C_lst.append([D,L])
# 1,2 방향끼리 리스트를 만들고 3,4 방향끼리 리스트를 만든다.
ew_lst = []
ns_lst = []
print(C_lst)

for i in C_lst:
    if i[0] == 1 or i[0] == 2:
        ew_lst.append(i)
    else :
        ns_lst.append(i)
max_width = ((max(ew_lst)[1])*(max(ns_lst)[1]))

# print(max_width)
small_l = []

for k in range(len(C_lst)):                         # ew 방향의 가장 큰 값의 인덱스
    if C_lst[k][1] == max(ew_lst)[1]:
        small_l.append(k)
for l in range(len(C_lst)):                         # ns 방향의 가장 큰 값의 인덱스
    if C_lst[l][1] == max(ns_lst)[1]:
        small_l.append(l)

ew_idx = small_l[0]
ns_idx = small_l[1]

min_width = (C_lst[ew_idx-4][1])*(C_lst[ns_idx+4][1])
print((max_width - min_width)*K)
# min_width = C_lst[(small_l[0]-4)][1] * C_lst[int(small_l[1])-2][1]
# min_width = (small_l[0]*small_l[1])
# print(min_width)
# print(max_width - min_width)
# 중복된 방향 중 두번째 * 중복된 방향 중 첫번째
# print((max_width)*K)
# # print(C_lst)
# print(ew_lst)
# print(ns_lst)