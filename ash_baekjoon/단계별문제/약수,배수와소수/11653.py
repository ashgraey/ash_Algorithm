'''
문제
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

'''
# def sieve_of_eratosthenes(n):
#     # 초기에 모든 수를 소수로 가정하고 True로 설정
#     is_prime = [True] * (n + 1)
#     # print(is_prime)
#     # 0과 1은 소수가 아니므로 False로 설정
#     is_prime[0] = is_prime[1] = False

#     # 2부터 시작하여 배수들을 제거하여 소수를 찾음
#     for i in range(2, int(n**0.5) + 1):
#         if is_prime[i]:
#             # i가 소수인 경우, i의 배수들을 모두 제거
#             for j in range(i*i, n + 1, i):
#                 is_prime[j] = False

#     # 소수들만 남기고 필터링
#     primes = [i for i in range(2, n + 1) if is_prime[i]]
#     return primes

# # 예시: 1부터 30까지의 소수 찾기
# n = 30
# primes = sieve_of_eratosthenes(n)
# print("1부터 {}까지의 소수: {}".format(n, primes))


import sys, math
input = sys.stdin.readline

# 에라토스테네스의 체 구현
def get_prime(n) :
    # 초기값 True
    is_prime = [True] * (n + 1)
    # 0과 1은 소수가 아니므로 False
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1) :
        if is_prime[i] :

            # i가 소수인경우, i의 배수들 제거
            for j in range(i*i, n + 1, i) :
                is_prime[j] = False
    
    # print(is_prime)
    return get_prime_num(is_prime)
    # return is_prime

def get_prime_num(is_prime) :
    prime_num = []
    for i in range(len(is_prime)) :
        if is_prime[i] == True :
            prime_num.append(i)
    
    return prime_num

n = int(input())
a = get_prime(n)
# print(a)
# n 소인수분해 
i = 0
while i < len(a) :
    if n % a[i] == 0 :
        n //= a[i]
        # print("n : ", n)
        print(a[i])
    else :
        i += 1





