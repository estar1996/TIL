# def factorial(n):
#     ans = 1
#     for i in range(2,n+1):
#         ans *= i
#     return ans
# def combination(n,k):
#     return factorial(n) / factorial(n-k)*factorial(k)
from itertools import combinations
N,K = map(int,input().split())
combi = list(combinations(range(N),K))
print(len(combi))
# print(combination(N,K))