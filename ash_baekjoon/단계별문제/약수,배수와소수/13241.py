'''
문제 최소공배수//
'''
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
tempA = a 
tempB = b

if a < b :
    temp = b
    b = a 
    a = temp

while b > 0 :
    a %= b

    temp = b
    b = a 
    a = temp

print(tempA * tempB // a)