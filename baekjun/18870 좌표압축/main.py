import sys
sys.stdin = open('input.txt')

N = int(input())
lst1 = list(map(int,input().split()))
lst = sorted(list(set(lst1)))
dic = {lst[i] : i for i in range(len(lst))}
for i in lst:
    print(dic[i],end=' ')