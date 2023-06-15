import sys

while 1:
    lst = list(map(int,sys.stdin.readline().split()))
    if lst == [0,0,0]:
        break
    lst = sorted(lst)
    if (lst[0]**2) + (lst[1] ** 2) == lst[2]**2:
        print('right')
    else:
        print('wrong')