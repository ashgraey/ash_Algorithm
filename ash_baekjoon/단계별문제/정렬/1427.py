'''
문제 소트인사이드//
'''

import sys

input = sys.stdin.readline
n = input().rstrip()

result = sorted(n, reverse=True)
# print(result)
result = ''.join(result)
print(int(result))