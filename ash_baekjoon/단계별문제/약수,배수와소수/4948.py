'''
문제 베르트랑 공준//
'''
import sys, math
input = sys.stdin.readline

def get_prime(n, n2) :
    prime_num = [True] * (n2 + 1)
    prime_num[0] = prime_num[1] = False

    # 2부터 n의 제곱근까지 소수인지 아닌지 판별
    for i in range(2, int(math.sqrt(n2) + 1)) :
        # prime_num[i] == True 소수
        if prime_num[i] :
            # i의 배수들은 False로 체크
            for j in range(i*i, n2+1, i) :
                prime_num[j] = False    
    
    prime_list = []
    for i in range(n + 1, n2 + 1) :
        if prime_num[i] :
            prime_list.append(prime_num[i])

    return prime_list       

while True :

    n = int(input())
    n2 = n * 2

    if n == 0 :
        break

    prime_num = get_prime(n,n2)
    print(len(prime_num))

# 시간초과남 에스테라토네스의 체를 써야할듯
# def get_prime(n, n2) :
#     prime_num = []
#     for i in range(n + 1, n2 + 1) :

#         # if i == 1 :
#         #     cnt = 1
        
#         # else :
#         cnt = 0
#         for j in range(2, int(math.sqrt(i)) + 1) :
#             if i % j == 0 :
#                 cnt += 1 

#         if cnt == 0 :
#             prime_num.append(i)
    
#     return prime_num
            

# while True :

#     n = int(input())
#     n2 = n * 2

#     if n == 0 :
#         break

#     prime_num = get_prime(n,n2)
#     print(len(prime_num))