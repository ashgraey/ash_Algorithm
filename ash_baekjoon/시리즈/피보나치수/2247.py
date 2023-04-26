'''
문제 피보나치수//
'''
import sys
input = sys.stdin.readline

n = int(input())

if n == 0 or n == 1 :
    print(n)

else :
    a = 0
    b = 1
    c = a + b
    for i in range(2, n) :
        a = b
        b = c
        c = a + b
    print(c)

