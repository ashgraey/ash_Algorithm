# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''
    s = s.split(" ")
    # print(s)
    for i in range(len(s)) :
        s[i] = int(s[i])
    # print(s)
    a = max(s)
    b = min(s)
    # print(a)
    answer += str(b)
    answer += " "
    answer += str(a)

    return answer

s = "1 2 3 4"
s = "-1 -2 -3 -4"
s = "-1 -1"
r = solution(s)
print(r)

# 음수도 인식해야하므로 형변환을 해서 저장하면된다. 
