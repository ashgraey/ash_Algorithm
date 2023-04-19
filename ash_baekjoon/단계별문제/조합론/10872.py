'''
문제 팩토리얼//
'''
import sys
input = sys.stdin.readline

n = int(input())
fac = 1
for i in range(n, 0, -1) :
    fac *= i
    # print(i)
print(fac)