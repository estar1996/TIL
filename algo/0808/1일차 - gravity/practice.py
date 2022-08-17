#gravity

import sys
sys.stdin = open('input3.txt')

lst = list(map(int,input().split()))


# for value in lst:
#     print(value)
res = 0
for idx in range(len(lst)):
    value = lst[idx]
    # 나보다 작은 박스무더기의 수를 세야함
    cnt = 0 #하나씩 더해줄 것

    # 나보다 오른쪽에 있는
    
    
    for right_idx in range(idx+1,len(lst)):
        if value > lst[right_idx]:
            cnt +=1
    
    if cnt > res:
        res = cnt

    
print(res)






# for idx, value in enumerate(lst):
