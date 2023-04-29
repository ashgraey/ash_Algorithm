'''
문제 이중우선순위 큐//
heap구조로 짜야하나봄
'''
import sys, heapq
input = sys.stdin.readline
tc = int(input())

def max_remove(q) :
    # max_val = heapq.heappop(-q)
    copy = []
    for i in range(len(q)) :
        heapq.heappush(copy, -q[i])
    
    max_val = heapq.heappop(copy)
    return -max_val

for _ in range(tc) :
    t = int(input())
    q = []
    for _ in range(t) :
        user = list(input().split())
        # print(user)
        user[-1] = int(user[-1])

        if user[0] == "I" :
            heapq.heappush(q, user[-1])
        
        # 최대값 heap을 구하는 
        if user[0] == "D" and user[-1] == 1 :
            if len(q) != 0 :
                max_val = max_remove(q)
                q.remove(max_val)
                

        # 최소값 heap을 구하는 heapop() 메소드 
        elif user[0] == "D" and user[-1] == -1 : 
            if len(q) != 0 :
                heapq.heappop(q)

        # print(q)
    
    if len(q) == 0 :
        print("EMPTY")
    else :
        print(max(q), min(q))

# 시간초과
# import sys
# from collections import deque

# input = sys.stdin.readline

# tc = int(input())

# for _ in range(tc) :
#     t = int(input())
#     q = deque()
#     for _ in range(t) :
#         user = list(input().split())
#         # print(user)
#         user[-1] = int(user[-1])

#         if user[0] == "I" :
#             q.append(user[-1])
        
#         # q.sort()
#         # q = sorted(q)
#         # q = deque(q)
#         if len(q) > 0 : 
#             maxQ = max(q)
#             minQ = min(q)
#         # print(maxQ, minQ)

#         if user[0] == "D" and user[-1] == 1 :
#             if len(q) != 0 :
#                 maxIdx = q.index(maxQ)
#                 # print(maxIdx)
#                 del(q[maxIdx])


#         elif user[0] == "D" and user[-1] == -1 : 
#             if len(q) != 0 :
#                 minIdx = q.index(minQ)
#                 del(q[minIdx])


#         # print(q)
    
#     if len(q) == 0 :
#         print("EMPTY")
#     else :
#         print(maxQ, minQ)