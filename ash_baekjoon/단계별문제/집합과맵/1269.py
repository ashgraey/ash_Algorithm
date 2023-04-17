'''
문제 대칭 차집합//
'''

import sys

input = sys.stdin.readline

a, b = map(int, input().split())

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

cnt = 0
for i in set_a :
    if i in set_b :
        cnt += 1
size_a = len(set_a) - cnt

cnt = 0 
for i in set_b :
    if i in set_a :
        cnt += 1 
size_b = len(set_b) - cnt

print(size_a + size_b)
# set_a.add(map(int, input().split()))
# print(set_a)