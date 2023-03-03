# https://school.programmers.co.kr/learn/courses/30/lessons/12934

'''
문제 설명
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

제한 사항
n은 1이상, 50000000000000 이하인 양의 정수입니다.

입출력 예
n	return
121	144
3	-1

입출력 예 설명
입출력 예#1
121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.

입출력 예#2
3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.
'''
import math
# def solution(n):
#     answer = 0 
#     num = 1
#     while True :
        
#         if num * num == n :
#             answer = (num + 1) * (num + 1)
#             break

#         if num > n :
#             answer = -1
#             break
#         num += 1
            
#     return answer
            
# n = 121
# a = solution(n)
# print(a)

# 내장함수 math.sqrt() 사용
def solution(n):
    # m = int(math.sqrt(n))
    # float형으로 return
    # 이걸 이용해 제곱근이 정수인지 확인
    if math.sqrt(n) - int(math.sqrt(n)) != 0 :
        answer = -1
    else :
        m = int(math.sqrt(n) + 1)
        m *= m
        answer = m
    return answer
            
# n = 121
n = 3
a = solution(n)
print(a)