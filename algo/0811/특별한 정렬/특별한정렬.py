from platform import java_ver
import sys
sys.stdin = open('sample_input(3).txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    new_lst = []

    for i in range(len(lst)):
        k = len(lst) - i
        for j in range(1,k):
            if lst[j-1] >= lst[j]:
                temp = lst[j-1]
                lst[j-1] = lst[j]
                lst[j] = temp
            
        
    for a in range(1,6):

       new_lst.append(lst[N-a])
       new_lst.append(lst[a-1])
   
    print(f'#{tc}',*new_lst)
   
        