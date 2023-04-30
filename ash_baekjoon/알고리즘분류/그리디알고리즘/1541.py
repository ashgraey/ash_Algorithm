'''
문제 잃어버린 괄호//

알고리즘 분류// 
그리디 알고리즘
문자열 파싱

모르겠다 어렵네;;
문제 해설//
split을 활용하면 어렵지 않게 풀수 있었던 문제 였던거 같다. 
아이디어는 80퍼 정도 생각했으나 -앞에서 괄호를 붙여주면됨 이게 구현까지 이르지 못한거 같다. 
쉽게 생각하면 초기 입력값에 split("-")를 해주면 일단 -기호를 기준으로 깔끔하게 split되었을텐데 구현부분의 미숙함이 느껴진다.
'''

import sys
input = sys.stdin.readline

words = input().rstrip()

words = words.split("-")
# print(words)

num = []
for i in words :
    cnt = 0 
    s = i.split("+") # i에 +기호가 없다면 정수 변환 후 바로 num으로 append된다.
    for j in s :
        cnt += int(j)
    
    num.append(cnt)

# print(num)
fir = num[0]
for i in range(1, len(num)) :
    fir -= num[i]

print(fir)

# 초기 구현 
'''
접근방식은 나쁘지 않았다. 일단 -를 기준으로 괄호를 씌우는데 까지는 성공했지만
괄호를 씌우는게 출력을 해야하는 부분이 아니어서 논점을 잘 알지 못한거 같다.
그리디보다도 오히려 문자열 파싱을 배운 부분이 큰거 같다.
'''
# cnt = 0 
# temp_word = ""
# for i, word in enumerate(words) :
#     if cnt == 0 and word == "-" :
#         temp_word += "-("
#         cnt += 1

#     elif cnt != 0 and word == "-" :
#         temp_word += ")-"
    
#     else :
#         temp_word += word
#     print(i)

# if (")" not in temp_word) and ("(" in temp_word):
#     temp_word += ")"        
    
# print(temp_word)
