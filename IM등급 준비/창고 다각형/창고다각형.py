import sys
from turtle import width
sys.stdin = open("input.txt")

N = int(input())

LH_lst = []                                                             # L : 위치  H : 높이        인풋받은 L,H 를 리스트로 묶어서 다시 넣을 리스트
for i in range(N):
    L,H = map(int,input().split())
    LH_lst.append([L,H])            

    

LH_lst.sort(key = lambda x:x[0])                                        # LH_lst 를   L 의 값에 따라 오름차순 정렬한다.
max_H = 0                                                               # 최대 높이를 구한다.
max_idx = 0                                                             # 최대 높이가 있는 인덱스를 구한다.
for k in range(N):                                                      # 최대 높이와 최대 높이가 있는 인덱스를 구함
    if LH_lst[k][1] > max_H:            
        max_H = LH_lst[k][1]
        max_idx = k



width = 0                                                               # 넓이 초기값

for j in range(1,max_idx+1):                                            # 최대 높이가 있는 idx까지 반복문을 돈다.
    temp = []                                                           #
#     if LH_lst[j-1][1] > LH_lst[j][1]:
#         width += (LH_lst[j-1][1]*(LH_lst[j][0]-LH_lst[j-1][0]))
#         temp.append(LH_lst[j-1])
#         LH_lst[j] = temp.pop()
# print(width)
    print(LH_lst[j][0]-LH_lst[j-1][0])
# for h in range(max_idx+1,N):
#     temp2 = []    
#     if LH_lst[N+1-max_idx][1] > LH_lst[N-max_idx][1]:
#         width += (LH_lst[N+1-max_idx][1]*(LH_lst[N-max_idx][0]-LH_lst[N+1-max_idx][0]))
#         temp2.append(LH_lst[N+1-max_idx])
#         LH_lst[N-max_idx] = temp2.pop()
# print(width)
# print(width)

# # print(LH_lst)