'''
문제 최소 힙//
'''
import sys, heapq
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n) :
    heap = int(input())

    if heap == 0 :
        if len(arr) == 0 :
            print(0)
        # print(min(arr))
        else :
            min = heapq.heappop(arr)
            print(min)
        # print(arr)
    
    elif heap != 0 :
        heapq.heappush(arr, heap)
    
    # print(arr)
    

