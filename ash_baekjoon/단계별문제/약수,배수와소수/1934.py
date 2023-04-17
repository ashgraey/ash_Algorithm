'''
문제 최소공배수//
'''

import sys
input = sys.stdin.readline

tc = int(input())

# # 기본적인 최소공배수 구하기, 런타임에러
# answer = []
# for _ in range(tc) :
#     a, b = map(int, input().split())

#     i = 1
#     while True :
#         if i % a == 0 and i % b == 0 :
#             result = i 
#             break
#         i += 1 

#     answer.append(result)

# for i in answer :
#     print(i)

# 유클리드 호제법
# 큰 수를 a에 담는다.
# a % b로 나눈다. a와 b의 값교체
answer = []
for _ in range(tc) :
    a, b = map(int, input().split())
    tempA = a
    tempB = b

    # a쪽을 항상 큰 수로, 최소공배수를 구하는 유클리드 호제법
    if a < b : 
        temp = a
        a = b
        b = temp
    
    while True :
        if b == 0 :
            break 
        
        a = a % b
        temp = b
        b = a
        a = temp
    
    # 최대공약수 : a * b // 최소공배수
    answer.append(tempA * tempB // a)

for i in range(tc) :
    print(answer[i])