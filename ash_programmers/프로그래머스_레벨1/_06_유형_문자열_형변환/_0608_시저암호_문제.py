# https://school.programmers.co.kr/learn/courses/30/lessons/12926
'''
문제 설명
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. 
"z"는 1만큼 밀면 "a"가 됩니다. 
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.

입출력 예
s	    n	result
"AB"	1	"BC"
"z"	    1	"a"
"a B z"	4	"e F d"

'''
# 좀 어려웠음 find()로 인덱스를 반환시키면 조금 쉬운듯 하다
def solution(s, n):
    answer = ''
    low = "abcdefghijklmnopqrstuvwxyz"
    upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in s :
        if char in low :
            idx = low.find(char) + n 
            idx = idx % 26 # 길이를 초과하는 경우에도 사용하기 위함
            answer += low[idx]
        elif char in upp :
            idx = upp.find(char) + n
            idx = idx % 26
            answer += upp[idx]
        else :
            answer += " " # 공백 일 경우

    return answer
    
s = "AB"
s = "aBz"
n = 1

a = solution(s , n)
print(a)

# 다른 사람 풀이
# find()함수 찾을 문자가 있으면 해당 인덱스의 값을 반환해줌
# def solution(s, n):
#     low = "abcdefghijklmnopqrstuvwxyz" # 소문자. 인덱스는 0에서 25
#     up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     answer = ''
#     for char in s:
#         if char in low:
#             ind = low.find(char) + n # low 문자열에서 찾은 해당 알파벳 인덱스 + n
#             print(ind)
#             answer += low[ind%26] # 26으로 나눈 나머지를 사용할 경우 25를 초과하는 경우도 활용 가능 => 찾은 알파벳이 z일 경우 인덱스는 25 + 1 26이므로 인데스를 초과함 그러나 % 26을 함으로써 맨 처음 인덱스인 0을 사용
#         elif char in up:
#             ind = up.find(char)+n
#             answer += up[ind%26]
#         else: # 공백일 경우도 고려
#             answer += " "
#     return answer
     
# result = solution("a B z E", 4) # 'e F d I'
# print(result)
