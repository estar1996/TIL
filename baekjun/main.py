import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(5)]
    print(arr)
    d_lst = []


    
    for i in range(5):
        for j in range(5):
            lst = []
            if i == j:
                lst.append(arr[i][j])
            for l in range(1,5):
                lst2 = []
                if i+l < 5 and j-l > 0:
                    lst.append(arr[i+l][j-l])
            for g in range(1,5):
                lst3 = []
                if i-g > 0 and j+g < 5:
                    lst.append(arr[i-g][j+g])
            d_lst.append(lst)
            d_lst.append(lst2)
            d_lst.append(lst3)

    print(d_lst)