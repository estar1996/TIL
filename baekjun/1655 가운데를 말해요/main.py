import sys
import heapq
input = sys.stdin.readline

N = int(input())
left_h, right_h = [],[]

for i in range(N):
    n = int(input())

    if len(left_h) == len(right_h):
        heapq.heappush(left_h, -n)
    else:
        heapq.heappush(right_h,n)

    if len(left_h) >= 1 and len(right_h) >= 1 and left_h[0] * -1 > right_h[0]:
        