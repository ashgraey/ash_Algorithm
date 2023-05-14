'''
문제 단어 뒤집기2//

알고립즘//
구현, 자료구조, 문자열, 스택

키포인트//
일단 너무 빡셌다..
1. 경우의 수를 두가지로 나눔 
    1 - 1) ">" 문자가 포함
    1 - 2) "<" 문자가 없음

1 - 1) 처리하기가 까다로웠음 괜히 2차 반복으로 하려다가 잘 안됨, 일단 조건문으로 해결
여기서 2차 관문이 있음 "<>"기준으로 split한 후에 "<>" 포함되지 않은 문자열중 공백이 들어가 있으면 잘라서 요소 하나하나 문자열을 뒤집어 줘야함
함수로 해결

1 - 2) 같은 로직이라 get_reverse() 함수로 해결
'''

import sys
input = sys.stdin.readline
def get_reverse(word) :
    arr_word = word.split(" ")
    # print(arr_word)

    result = []
    for v in arr_word :
        v_reverse = v[::-1]
        result.append(v_reverse)

    return result

word = input().rstrip()
# print(len(word))


if "<" in word :
    result = []
    temp = ""
    for i in range(len(word)) :
        if word[i] == "<" :
            if len(temp) != 0 :
                result.append(temp)
                temp = ""
            temp += word[i]
        
        elif word[i] == ">" :
            temp += word[i]
            result.append(temp)
            temp = ""
        else :
            temp += word[i]
    if temp != "" :
        result.append(temp)
    # print(result)

    for i in range(len(result)) :
        if "<" not in result[i] :
            reverse = get_reverse(result[i])
            result[i] = " ".join(reverse)
    
    for v in result :
        print(v, end = "")
        
else :
    result = get_reverse(word)
    
    for v in result :
        print(v, end = " ")
    # print(result)

# 2차 반복으로 하려다가 망함
# if "<" in word :
#     result = [] 
#     idx = 0
#     # temp = ""
#     cnt = 0
#     while idx < len(word):
        
#         if word[idx] == "<" :
#             temp = ""
#             for j in range(idx, len(word)) :
#                 temp += word[j]
#                 if word[j] == ">" :
#                     idx = j + 1
#                     result.append(temp)
#                     break
#         else :
#             temp = ""
#             for k in range(idx, len(word)) :
#                 if word[k] == "<" :
#                     idx = k
#                     result.append(temp)
#                     break
#                 temp += word[k]
#         print(idx)
        
    
        
#     print(cnt)    
#     print(result)


# # 문자열 안에 "<" 포함 안되어 있는 경우
# else :
#     arr_word = word.split(" ")
#     # print(arr_word)

#     result = []
#     for v in arr_word :
#         v_reverse = v[::-1]
#         result.append(v_reverse)
    
#     for v in result :
#         print(v, end = " ")
#     print(result)