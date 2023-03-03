# https://school.programmers.co.kr/learn/courses/30/lessons/12930
'''
문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다.
각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
# 각 단어의 짝수번째가 upper, 홀수번째가 lower

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

입출력 예
s	                return
"try hello world"	"TrY HeLlO WoRlD"
'''


# 1차 시도 실패 : 원인 = 각 단어로 해결했어야 했는데 문장 하나를 단어로 생각함
# 홀수 소문자, 짝수 대문자
# 소문자로 받으니깐 짝수만 upper()로 대문자로 만들어보자
# def solution(s):
#     answer = ''
#     # s = s.upper()
#     # print(s[0])
#     for i in range(len(s)) :
#         if i % 2 == 0 :
#             answer += s[i].upper()
#             # print(s[i])
#         else :
#             answer += s[i]

#     return answer

# s = "try hello world"
# a = solution(s)
# print(a)

# 각 단어의 짝수번째, 홀수번째가 중요!!!
def solution(s):
    answer = ''
    sList = s.split(" ")
    print(sList)

    main = ""
    for i in range(len(sList)) :
        temp = ""
        for j in range(len(sList[i])) :
            if j % 2 == 0 :
                temp += sList[i][j].upper()
            else :
                temp += sList[i][j].lower()
        
        main += temp + " "
        answer = main[:-1]
    return answer

s = "try hello world"
a = solution(s)
print(a)