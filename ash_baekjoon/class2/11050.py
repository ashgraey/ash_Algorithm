'''
문제 이항계수//
자연수 
\(N\)과 정수 
\(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 
\(N\)과 
\(K\)가 주어진다. (1 ≤ 
\(N\) ≤ 10, 0 ≤ 
\(K\) ≤ 
\(N\))

출력
 
\(\binom{N}{K}\)를 출력한다.


'''
# 이항계수를 구하는 공식(n, k)
# 5! = 1 * 2 * 3 * 4 * 5
# C(5,2) = 5! / (2! * 3!) = 10

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

min = n - k

def total(arr) :
    tot = 1 
    for i in arr :
        tot *= i

    return tot 


totN = total([i for i in range(1, n + 1)])
totK = total([i for i in range(1, k + 1)])
totMin = total([i for i in range(1, min + 1)])
# print(totMin, totN, totK)
print(totN // (totK * totMin))


