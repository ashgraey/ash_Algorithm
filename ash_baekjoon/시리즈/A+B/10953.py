'''
A + B - 6
'''

import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    num = input().rstrip()
    num = num.split(",")
    num[0] = int(num[0])
    num[1] = int(num[1])
    print(sum(num))