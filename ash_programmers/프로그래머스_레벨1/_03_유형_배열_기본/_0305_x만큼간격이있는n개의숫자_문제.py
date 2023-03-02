# https://school.programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    answer = []

    for i in range(n) :
        num = x + (x * i)
        answer.append(num)
    
    return answer

# x = 2
# n = 5
x = int(input())
n = int(input())
answer = solution(x , n)
print(answer)

# x : 시작하는 수
# n : 개수