import sys
sys.stdin = open("input.txt")

T = int(input())
# def haha(n):
#     for a in range(len(n_lst)):
#         if n_lst[a][0] == n:
#             new_lst.append(n_lst[a])
#         if n_lst[a][1] == n:
#             new_lst.append(n_lst[a])



for tc in range(1,T+1):
    E,N = map(int,input().split())
    lst = list(map(int,input().split()))

    n_lst = []
    for i in range(len(lst)//2):
        ll = []
        ll.append(lst[i * 2])
        ll.append(lst[i * 2 + 1])
        n_lst.append(ll)



    new_lst = []
    temp = N
    for _ in range(len(n_lst)+1):
        for j in range(len(n_lst)):
            if n_lst[j][0] == temp:
                if n_lst[j] == new_lst[-1]:
                    pass
                else:
                    new_lst.append(n_lst[j])
                    temp = n_lst[j][1]
            # if len(new_lst) == 0:
            #     result = 1
            if n_lst[j][1] == temp:
                new_lst.append(n_lst[j])


    if len(new_lst) == 1:
        print("#{} {}".format(tc,1))
    else:
        result = []
        for l in range(len(new_lst)):
            result.append(new_lst[l][0])
            result.append(new_lst[l][1])
        # print(len(set(result)))
        print(result)

