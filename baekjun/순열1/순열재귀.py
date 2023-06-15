# def f(i,k):
#     if i == k:      # 인덱스 i == 원소의 개수
#         print(p)
#     else:
#         for j in range(i,k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1,k)
#             p[i], p[j] = p[j], p[i]
#
#
#
# p = [1,2,3,4,5]
# f(0,4)
def f(i,k,r):
    global p
    if i == r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i+1,k,r)
                used[j] = 0






N = 5
R = 3
a = [i for i in range(1,N+1)]
used = [0] * N
p = [0] * R
f(0,N,3)