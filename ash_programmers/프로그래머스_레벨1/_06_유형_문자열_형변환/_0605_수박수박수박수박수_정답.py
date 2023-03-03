# https://school.programmers.co.kr/learn/courses/30/lessons/12922
def solution(n):
    answer = ''
    temp = "수박"
    for i in range(n):
        # 인덱스로 값을 정해서 넣음 
        # 짝수에는 "수", 홀수에는 "박"
        # 조건문을 안 써도 됨
        answer += temp[i % 2]

    return answer


n = 3
a = solution(n)
print(a)