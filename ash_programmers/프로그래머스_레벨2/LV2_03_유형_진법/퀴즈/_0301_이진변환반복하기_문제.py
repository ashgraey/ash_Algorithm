
# https://school.programmers.co.kr/learn/courses/30/lessons/70129
def get_one(s) :

    st = ''
    for num in s :
        if num != "0" :
            st += num
    # print("st : ", st)
    return st

def get_binary(a) :
    # 6 => 이진수변환

    # 1. a보다 큰 2의 배수를 만든다.
    b = 1
    while a >= b :
        b *= 2 
    # print(a, b)
    
    # 2. a = 6, b = 8 
    st = ''
    while True :
        if b == 0 :
            break

        s = a // b
        st += str(s)

        a = a % b
        b //= 2
    
    # print(st[1:])
    st = st[1:]
    return st


def solution(s):
    answer = [0,0]
    while True :
    # for i in range(3) :
        if s == "1" :
            break
        
        tempstr = s
        s = get_one(s)

        answer[0] += 1 
        answer[1] += len(tempstr) - len(s)
        # print(answer)
        # print(len(s))
        s = get_binary(len(s))
        # print("s : ", s)
        # break
    
    return answer

# s = "110010101001"
# s = "01110"
s = "1111111"
r = solution(s)
print(r)

"""
이진법 변환을 한다.
"""
# 1. 6보다 큰 2의 배수를 구한다.
# a = 1
# b = 6
# while b > a :
#     a *= 2
# print(a)

# # 받은 길이의 값을 2진수로 전환한다.
# st = ''
# # a = 8, b = 6
# while True :
#     if a == 0 :
#         break

 
#     s = b // a
#     st += str(s)

#     b %= a
#     a //= 2

# print(st[1:])