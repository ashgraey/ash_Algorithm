'''
문제 최대공약수//
'''

'''
해설//
입력의 제한이 너무 커서 반복문을 돌리거나 "111.."로 숫자를 변환하려는 경우 메모리가 초과함
규칙성을 찾아내는게 중요하다.

** 핵심
입력받는 a, b의 최대공약수가 1의 갯수이다!!
'''
import sys
input = sys.stdin.readline

# 정답
def gcd(a, b):
    while b: # b == 0 이면 False 즉 b가 0이되면 종료
        a, b = b, a % b
    return a  

a, b = map(int, input().split())

print('1' * gcd(a, b))

# 이것도 시간초과
# def gcd(a, b) : 
#     if a < b : 
#         a, b = b, a
    
#     while True :
#         if b == 0 :
#             break
        
#         a = a % b 
#         a, b = b, a
    
#     return a

# A, B = map(int, input().split())

# print(int("1" * gcd(A, B)))

# 재귀로 풀었더니 시간초과라니..
# def gcd(a, b) : 
#     if b == 0 : 
#         return a
#     else :
#         return gcd(b, a % b)

# a, b = map(int, input().split())
# # cnt = gcd(A,B)
# # print(cnt)
# print(int("1" * gcd(a, b)))


# if a < b : 
#     a, b = b, a

# while True :
#     if b == 0 :
#         break

#     a = a % b
#     a, b = b, a
# print(a)
# print(2 ** 63)