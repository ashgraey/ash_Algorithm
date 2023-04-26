# https://school.programmers.co.kr/learn/courses/30/lessons/12911
'''
수를 += 1씩 하면서 
이진수로 변환하고 
1의 갯수가 같은지 counting
'''
def n_count(n) :
    a = 1
    while n > a :
        a *= 2
    # print(a)

    st = ''
    while True :
        
        if n == 0 : 
            break 
        c = n // a
        st += str(c)

        n = n % a
        a = a // 2
        # print(a)
    st = st[1:]
    # print(st)
    st_cnt = st.count("1")
    return st_cnt

def solution(n):
    # n을 2진수로 변환 
    
    st_cnt = n_count(n)
    
    i = 1
    while True :
        big_cnt = n_count(n + i)

        if big_cnt == st_cnt :
            answer = n + 1 
            break
        i += 1

    return answer


n = 78
r = solution(n)
print(r)