# https://school.programmers.co.kr/learn/courses/30/lessons/12951

'''
틀린 코드 해설//
s의 요소인 v을 뒷 문자열을 검사하기 위해 반복문을 돌림 
이 과정에서 뭔가 예외처리가 잘 안된거 같음 복잡하게 풀려고 하니 더 안된 케이스 
슬라이싱을 좀 더 잘 사용했다면...
'''
# def solution(s):
#     answer = ""
#     abc = "abcdefghijklmnopqrstuvwxyz"
#     abc2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     sList = s.split(" ")
#     # print(sList)
#     for v in sList :
#         if v != "" :
#             for i in range(len(v)) : # 조금 더 심플하게 생각했으면 굳이 반복문을 돌려서 검사하지 않아도 되는걸 반복문을 돌려야한다고 생각함
#                 if i == 0 and v[i] in abc :
#                     up = v[0].upper()
#                     answer += up
                
#                 elif v[i] in abc2 :
#                     lo = v[i].lower()
#                     answer += lo
                
#                 else :
#                     answer += v[i]
        
#         answer += " "
#     answer[:-1]
#     return answer

# # s = "     3people     unFollowed     me"	
# # s = "for the last week"
# s = "3people unFollowed me"	
# r = solution(s)
# print(r)


def solution(s) :
    answer = ""
    s = s.split(" ")

    for v in s : 
        if v != "" :
            up = v[0].upper()
            lo = v[1:].lower() 
            answer += up
            answer += lo
        
        answer += " "

    return answer[:-1]
s = "for the last week"
s = "     3people     unFollowed     me"
s = "3people     unFollowed     me"
r = solution(s)
print(r)

# 공백이 여러줄이 있는 함정이 있다. 