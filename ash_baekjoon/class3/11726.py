'''
문제 2*n 타일링//
피보나치 수열로 풀면 간단함
'''
import sys
input = sys.stdin.readline

n = int(input())

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

print(answer % 10007)
