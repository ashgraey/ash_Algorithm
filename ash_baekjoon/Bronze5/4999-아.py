'''
문자열 길이 비교 문제
'''

# 입력은 2개 데이터 타입 : 문자열(str)

jae = input()
doc = input()

jae_len = len(jae)
doc_len = len(doc)

if jae_len > doc_len or jae_len == doc_len :
    print("go")
else :
    print("no")
