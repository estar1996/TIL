import sys
sys.stdin = open('sample_input(1).txt')

def max_sum(lst):
    max_num = lst[0]
    for i in lst:
        if i > max_num :
            max_num = i
    return max_num

def min_sum(lst):
    min_num = lst[0]
    for i in lst:
        if i > min_num :
            min_num = i
    return min_num

T = int(input())
for tc in range(1,T+1):

    N,M = map(int, input().split())

    a_lst = list(map(int,input().split()))

    res_lst=[]
    for i in range(0,N-M+1):        
        res = 0
        for a in range(i,M+i):
            res += a_lst[a]
        res_lst.append(res)

    print("#{} {}".format(tc,max(res_lst)-min(res_lst)))

