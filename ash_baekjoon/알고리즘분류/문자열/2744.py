'''
문제 대소문자 바꾸기//

알고리즘//
문자열, 구현
'''

word = input()

capital = "ABCDEFGHUIJKLMNOPQRSTUVWXYZ"

result = ""
for v in word :
    if v in capital :
        result += v.lower()
    else :
        result += v.upper()
    
print(result)
