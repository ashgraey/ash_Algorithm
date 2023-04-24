# https://school.programmers.co.kr/learn/courses/30/lessons/12914
'''
피보나치 수열
1 1 2 3 5 8 13 21 34
0 1 2 3 4 5 6  7  8

4칸  ; 5
1 : 1, 1, 1, 1
2 : 1, 2, 1 
3 : 1, 1, 2
4 : 2, 1, 1
5 : 2, 2

3칸 ; 3
1 : 1, 1, 1
2 : 1, 2
3 : 2, 1
'''

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

    return answer % 1234567

n = 4
# n = int(input())
r = solution(n)
print(r)



"""
피보나치 수열이다. 
"""