# https://school.programmers.co.kr/learn/courses/30/lessons/68935
'''
문제 설명
자연수 n이 매개변수로 주어집니다. 
n을 3진법 상에서 앞뒤로 뒤집은 후, 
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.

입출력 예
n	result
45	7
125	229
'''
# 인터넷 풀이
# def solution(n):
#     # answer = 0
#     result = ""
#     while n :
#         result += str(n % 3)
#         n = n // 3
    
#     # print(result)
#     return int(result, 3) # 10진법으로 변환
    
# n = 45
# result = solution(n)
# print(result)

# 강사님 정답
def solution(n):
    answer = 0
    a = ""
    temp = n
    b = 1
    while True:
        # print(temp)
        a += str(temp % 3)
        temp = temp // 3
        if temp == 0:
            break
        b *= 3
    # print("b : " , b)
    # print("a : " , a)
    # 3진법 -> 10진법 변환
    for i in range(len(a)):
        c = int(a[i]) * b
        answer += c
        b //= 3
    return answer
n = 45
result = solution(n)
print(result)