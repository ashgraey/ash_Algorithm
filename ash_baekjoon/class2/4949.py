'''
문제 균형잡힌 세상//
세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.

정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.

문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

입력
각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"), 대괄호("[ ]")로 이루어져 있으며, 온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.

입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.
출력
각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
'''

# a = [1, 2, 3, 4, 5]
# apop = a.pop()
# print(apop)
# print(a)
# hint : stack에 관한 문제
# pop()을 하면 맨 마지막 요소를 원본에서 추출 원본이 바뀜
# import sys
# input = sys.stdin.readline

# 입력값이 "." 이면 반복문 종료
while True :

    line = input()

    # print(line)
    if line == "." :
        break
    
    stack = []

    for v in line :
        if v == "(" or v == "[" :
            stack.append(v)
        
        elif v == "]" : 
            if len(stack) != 0 and stack[-1] == "[" :
                stack.pop()
            else :
                stack.append(v)

        elif v == ")" :
            if len(stack) != 0 and stack[-1] == "(" :
                stack.pop()
            else :
                stack.append(v)  
    
    # print(len(stack))
    if len(stack) == 0 :
        print("yes")
    else :
        print("no")
        
 
# chat GPT 정답
# .일때의 예외처리가 없어서 틀렸습니다. 나옴
# import sys
# for line in sys.stdin:
#     if line.strip() == '.':  # 입력의 종료조건인 '.'이 입력되면 종료합니다.
#         break
    
#     stack = []  # 스택 초기화
#     balanced = True  # 균형여부 초기화
    
#     for char in line:
#         if char in '([':  # 왼쪽 괄호라면 스택에 넣습니다.
#             stack.append(char)
#         elif char in ')]':  # 오른쪽 괄호라면
#             if not stack:  # 스택이 비어있다면 균형이 맞지 않습니다.
#                 balanced = False
#                 break
#             top = stack.pop()  # 스택에서 괄호를 꺼냅니다.
#             if (char == ')' and top == '(') or (char == ']' and top == '['):
#                 continue  # 괄호가 짝이 맞으면 다음 문자를 읽습니다.
#             else:
#                 balanced = False  # 괄호가 짝이 맞지 않으면 균형이 맞지 않습니다.
#                 break
    
#     if balanced and not stack:  # 모든 문자열을 읽고 스택이 비어있다면 균형이 맞습니다.
#         print('yes')
#     else:
#         print('no')
