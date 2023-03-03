# https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    a = 1
    b = n # 3
    c = m # 12

    # 큰 값을 m으로 설정
    if n > m:
        temp = n
        n = m
        m = temp

    # 최대 공약수
    while True:       
        check = False
        # 작은 값까지만 돌림
        for i in range(2, n + 1):
            if m % i == 0 and n % i == 0:
                a *= i
                m //= i # ?
                n //= i # ?
                check = True
                print("aa : " , a , " " , m , " " , n)
                break
        if check == False:
            break
    answer.append(a)
    
    # 최소 공배수
    i = b
    while True:
        if i % b == 0 and i % c == 0:
            break
        i += 1
    #print(i)
    answer.append(i)
    return answer

n = 36
m = 120
a = solution(n, m)
print(a)