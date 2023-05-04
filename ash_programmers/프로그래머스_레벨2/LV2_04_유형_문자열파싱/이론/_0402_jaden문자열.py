
"""
    [1] 아래문자열을 첫글자는 대문자로 나머지는 소문자로 변환하시오.
    [2] 단 , 공백을 그대로 유지한다.
    [3] 첫글자가 숫자면 숫자를 유지한다. 

    [예시]
        [1] "     3people     unFollowed     me  "
        [2] "     3people     Unfollowed     Me  "

"""

s = "     3people     unFollowed     me  "	
print(s)

# s = s.split(" ")
# # print(s)

# num = "0123456789"

# for i in range(len(s)) :
#     if s[i] != "" :
#         if s[i][0] not in num :
#             low = s[i][0]
#             up = s[i].upper()
#             s[i] = s[i].replace(low, up[0]) # 문자열 대체 : 1번 인자(변경하고자하는 값), 2번 인자(변경할 값)
#             # print(up[0])
#             # print(low)
#         # else :
#         #     pass
#     # print(s[i][0])
# s = ' '.join(s)
# print(s)        

# 쌤 답
s = s.split(" ")
#print(s)

for i , v in enumerate (s):
    if v != '':
        a = v[0].upper()
        b = v[1:].lower()
        s[i] = (a + b) + " " # 마지막 글자는 공백이 한칸 더들어갈수밖에 없다. 추후에 삭제한다.
print(s)

st = ""

for i , v in enumerate(s):
    if v == '':
        st += " "
    else:
        st += v

print(st)
st = st[:-1] # 마지막 공백 삭제
print(st)