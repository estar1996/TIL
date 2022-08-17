import sys
sys.stdin = open('input.txt')

def max_1(lst):
    for i in range(len(lst)):
        if lst[i] > lst[i+1]:
            lst[i+1] = lst[i]
    return lst[i+1]
T = int(input())

for tc in range(1,T+1):
    str1 = list(input())
    str2 = list(input())

    res =[0] *(len(str1))
    for idx in range(len(str1)):
        for i in range(len(str2)):
            if str1[idx] == str2[i]:
                res[idx] += 1

    print(max_1(res))
