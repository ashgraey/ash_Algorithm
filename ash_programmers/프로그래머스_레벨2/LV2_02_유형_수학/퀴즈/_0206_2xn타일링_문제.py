# https://school.programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    answer = 0
    if n == 1 or n == 2 :
        answer = n
    
    else :
        a = 1
        b = 2
        c = a + b
        for i in range(3, n) :
            a = b
            b = c
            c = a + b
        answer = c
    
    return answer % 1000000007

n = 4
# n = int(input())
r = solution(n)
print(r)

"""
피보나치 수열
0 1 2 3 5 8 13 21 34 55  
0 1 2 3 4 5 6  7  8  9
"""