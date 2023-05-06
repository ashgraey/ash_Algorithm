
# https://school.programmers.co.kr/learn/courses/30/lessons/17677
'''
키워드//
자카드 유사도

"FRANCE", "FRENCH"
{FR, RA, AN, NC, CE}, {FR, RE, EN, NC, CH}

주의점!
영문자로 된 글자 쌍만 유효하다.
그 외는 모두버린다.
비교시 대문자 소문자는 같은 원소로 취급

일단 틀렸습니다.
구현의 부족함 예외처리를 일일이 하려다보니 오히려 문제가 생김
테스트 케이스 4개는 통과했으나 정확성 테스트에서 통과를 못함
문제가 길면 뭘 우선적으로 해야하는지 아직 감을 잘 못잡는듯ㅜㅜ
구조적으로 생각하려는 힘을 기르자!
'''
# 정확성 61.5 테스트 통과 X
def get_arr(str1, str2) :
    arr = []
    for i in str1 :
        arr.append(i)
    for i in str2 :
        arr.append(i)
    
    return arr

def get_wordArr(word) :
    wordArr = []
    sample = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(len(word) - 1) :
        temp = ""
        cnt = 0 
        if word[i] in sample :
            temp += word[i]
            cnt += 1 
        if word[i + 1] in sample :
            temp += word[i + 1]
            cnt += 1 

        if cnt == 2 :    
            wordArr.append(temp)
        
    return wordArr
    
def solution(str1, str2):
    # arr_str1 = []
    # arr_str2 = []
    # 시작부터 대문자를 만들고 시작해보자
    str1 = str1.upper()
    str2 = str2.upper()

    arr_str1 = get_wordArr(str1)
    arr_str2 = get_wordArr(str2)
    # print(arr_str1)
    # print(arr_str2)
    
    
    if len(arr_str1) == 0 and len(arr_str2) == 0 :
        return 65536
    
    # 두집합의 합
    arr = get_arr(arr_str1, arr_str2)
    # print(arr)

    # 교집합 
    intersection = list(set(arr_str1) & set(arr_str2))
    print(intersection)
    
    # 합집합
    combination = set(arr) # 합집합
    combination = list(combination)
    print(combination)

    # 다중집합에 대한 예외처리
    # temp = arr[0]
    # cnt = 1 
    # for i in range(1, len(arr)) :
    #     if temp == arr[i] :
    #         cnt += 1 
    #         temp = arr[i]
        # print("cnt", cnt)

    # tot = []
    # if cnt == len(arr) :
    #     tot.append(len(arr_str1))
    #     tot.append(len(arr_str2))
    #     intersection = min(tot)
    #     combination = max(tot)
    #     # print(intersection, combination) 
    #     jaccard = intersection / combination

    # else :
    jaccard = len(intersection) / len(combination)



    
    return int(jaccard * 65536)
    
# str1 = "aa1+aa2"
# str1 = "E=M*C^2"
# str1 = "FRANCE"
# str2 = "french"
# str1 = "handshake"
# str2 = "shake hands"
str1 = "aa1+aa2"
str2 = "AAAA12"
# str1 = "E=M*C^2"
# str2 = "e=m*c^2"
r = solution(str1, str2)
print(r)