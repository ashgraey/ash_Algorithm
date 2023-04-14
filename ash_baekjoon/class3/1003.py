'''
피보나치 함수//
'''
# # 시간초과
# def fibonacci(n) :
#     cnt0 = 0
#     cnt1 = 0
#     cntList = [0,0]
#     if n == 0 :
#         # print(0)
#         cnt0 += 1
#         cntList[0] += cnt0
#         return cntList
#     elif n == 1 :
#         cnt1 += 1
#         cntList[1] += cnt1
#         return cntList
#     else :
#         return fibonacci(n - 1) + fibonacci(n - 2)

# import sys
# input = sys.stdin.readline

# tc = int(input())

# for _ in range(tc) :
#     n = int(input())
#     # print(fibonacci(n))
    
#     temp = fibonacci(n)
#     tot1 = 0
#     tot2 = 0
#     for i in range(len(temp)) :
#         if i % 2 == 0 :
#             tot1 += temp[i]
#         else :
#             tot2 += temp[i]
    
#     print(tot1, tot2)