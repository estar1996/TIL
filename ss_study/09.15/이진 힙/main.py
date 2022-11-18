import sys
sys.stdin = open("input.txt")


def enq(n):
    global last
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가
    c = last
    p = c // 2      # 완전 이진 트리 부모 정점 번호
    while p and heap[p] < heap[c]:
        heap[p],heap[c] = heap[c],heap[p]
        c = p
        p = c//2
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    heap = [0]*(N+1)
    last = 0
    enq(1)
    print(lst)