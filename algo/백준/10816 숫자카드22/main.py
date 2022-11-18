# import sys
#
# N = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# checks = list(map(int, sys.stdin.readline().split()))
# cards.sort()
# def binary_search(arr,target,start,end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if arr[mid] < target:
#         return arr[start:end +1].count(target)
#     elif arr[mid] < target:
#         return binary_search(arr,target,mid+1,end)
#     else:
#         return binary_search(arr,target,start,mid-1)
#
# for i in range(len(checks)):
#     a = binary_search(cards,checks[i],0,len(cards)-1)
#     if a is not None:
#         print(a, end=' ')
#     else:
#         print(0,end=' ')

from collections import Counter
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

count = Counter(card)

for i in range(len(test)):
    if test[i] in count:
        print(count[test[i]], end=' ')
    else:
        print(0, end=' ')