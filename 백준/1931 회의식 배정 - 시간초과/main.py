import sys
sys.stdin = open("input.txt")

T = int(input())


all_lst = []
for tc in range(1,T+1):
    s_f = list(map(int,input().split()))
    all_lst.append(s_f)

lst = sorted(all_lst)

st_lst = []

for i in range(len(lst)):
    cnt = 1
    temp = lst[i][1]
    for j in range(i+1,len(lst)):
        if lst[j][0] > temp:
            cnt += 1
            temp = lst[j][1]
        if i == (len(lst)-1):
            break
    st_lst.append(cnt)


print(max(st_lst))