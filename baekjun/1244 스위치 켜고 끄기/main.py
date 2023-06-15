import sys
sys.stdin = open('input.txt')

N = int(input())
s_lst = list(map(int,input().split()))
s_num = int(input())
lst = []
for _ in range(s_num):
    s = list(map(int,input().split()))
    lst.append(s)

for i in range(s_num):
    if lst[i][0] == 1:
        for j in range(len(s_lst)):
            if (j+1) % lst[i][1] == 0:
                if s_lst[j] == 1:
                    s_lst[j] = 0
                elif s_lst[j] == 0:
                    s_lst[j] = 1
    elif lst[i][0] == 2:
        if s_lst[lst[i][1]-1] == 1:
            s_lst[lst[i][1]-1] = 0
        elif s_lst[lst[i][1]-1] == 0:
            s_lst[lst[i][1]-1] = 1
        if len(s_lst) - lst[i][1] > lst[i][1] :
            for l in range(1,len(s_lst) - lst[i][1]):
                if s_lst[lst[i][1] + l-1] == s_lst[lst[i][1] -l-1]:
                    if s_lst[lst[i][1] + l-1] == 1:
                        s_lst[lst[i][1] + l-1] = 0
                        s_lst[lst[i][1] - l-1] = 0
                    elif s_lst[l] == 0:
                        s_lst[lst[i][1] + l-1] = 1
                        s_lst[lst[i][1] - l-1] = 1
        else:
            for l in range(1,lst[i][1]):
                if s_lst[lst[i][1] + l-1] == s_lst[lst[i][1] -l-1]:
                    if s_lst[lst[i][1] + l-1] == 1:
                        s_lst[lst[i][1] + l-1] = 0
                        s_lst[lst[i][1] - l-1] = 0
                    elif s_lst[j] == 0:
                        s_lst[lst[i][1] + l-1] = 1
                        s_lst[lst[i][1] - l-1] = 1
print(s_lst)