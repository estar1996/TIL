import sys
sys.stdin = open("input.txt")


def inorder(n):
    global res
    if n == 0:
        return
    cnt+=1
T = int(input())

for tc in range(1,T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    for i in range(0,E):
        left[i] = lst[i*2]
        right[i] = lst[i*2+1]
    res = 0

    # print(n_lst)
    print(left)
    print(right)