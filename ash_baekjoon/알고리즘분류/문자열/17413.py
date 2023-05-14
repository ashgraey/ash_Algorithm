'''
문제 단어 뒤집기2//

알고립즘//
구현, 자료구조, 문자열, 스택

키포인트//

'''

import sys
input = sys.stdin.readline

word = input().rstrip()

if "<" in word :
    result = [] 
    idx = 0
    # temp = ""
    cnt = 0
    while idx < len(word) :
        
        if word[idx] == "<" :
            temp = ""
            for j in range(idx, len(word)) :
                temp += word[j]
                if word[j] == ">" :
                    idx = j + 1
                    result.append(temp)
                    break
        else :
            temp = ""
            for i in range(idx, len(word)) :
                if word[i] == "<" :
                    idx = i + 1 
                    result.append(temp)
                    break
                temp += word[i]
            
        
    
        
    print(cnt)    
    print(result)


# 문자열 안에 "<" 포함 안되어 있는 경우
else :
    arr_word = word.split(" ")
    # print(arr_word)

    result = []
    for v in arr_word :
        v_reverse = v[::-1]
        result.append(v_reverse)
    
    for v in result :
        print(v, end = " ")
    # print(result)