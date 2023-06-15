import sys
sys.stdin = open("input.txt")

N = int(input())
lst = []

for _ in range(N):

    a,b,c,d = map(str,input().split())
    lst.append([a,int(b),int(c),int(d)])



res_lst = sorted(lst, key=lambda x : (-x[1], x[2], -x[3], x[0]))

for score in res_lst:

    print(score[0])