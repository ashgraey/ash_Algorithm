'''
문제 카드1//
'''

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr_n = deque([i for i in range(1, n + 1)])
# print(arr_n)
# print(len(arr_n))

answer = []
while True : 
    # print(arr_n.popleft())
    answer.append(arr_n.popleft())
    
    if len(arr_n) == 0 :
        break
    
    temp = arr_n.popleft()
    arr_n.append(temp)

    # print(arr_n)
    
# print(answer)
for i in answer : 
    print(i, end = " ")


