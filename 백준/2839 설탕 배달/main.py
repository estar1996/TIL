import sys
sys.stdin = open("input.txt")




# print((N//5) + ((N % 5) // 3))
# if N % 5 == 0:
#     print(N//5)
# elif N % 5 != 0:
#     if (N % 5) % 3 == 0:
#         print((N//5) + ((N % 5) // 3))
#     else:
#         if N % 3 == 0:
#             print(N//3)
#         else:
#             for i in range(N//3+1):
#                 for j in range(N//3+1):
#                     if (N % (3*i)) + (N % (5*j)) == 0:
#                         print(i+j)
#                     else:
#                         print(-1)

N = int(input())
lst = []
for i in range(N//3 + 1):
    for j in range(N // 3 + 1):
        if 3*i + 5*j == N:
            lst.append(i+j)
        else:
            lst.append(2000)



if min(lst) == 2000:
    print(-1)
else:
    print(min(lst))