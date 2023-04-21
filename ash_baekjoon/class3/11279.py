'''
문제 최대힙//

파이썬 heapq모듈에는 최소값만을 구하는 함수
heapq.heappop()밖에 없다.
최대값을 반환하고 제거하려면 입력값에 -(minus)를 하고 똑같이 heappop()을 사용한 후 
print시 다시 양수로 변환하여 출력하면 된다.
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
        else : 
            max = heapq.heappop(arr)
            print(-max)
    
    else :
        heapq.heappush(arr, -heap)
    
    # print(arr)    