import sys
sys.stdin = open('input.txt')

lst = input().split('-')

sum_lst = []

for i in lst:
    cnt = 0
    h_lst = i.split('+')
    for j in h_lst:
        cnt += int(j)
    sum_lst.append(cnt)
sum_cnt = sum_lst[0]
for i in range(1,len(lst)):
    sum_cnt -= sum_lst[i]


print(sum_cnt)