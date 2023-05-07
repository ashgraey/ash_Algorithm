'''
문제 열 개씩 끊어서 제출//

알고리즘//
문자열
구현

키포인트//
슬라이싱을 사용해보고 싶다.
'''

import sys
input = sys.stdin.readline

n = input().rstrip()

size = (len(n) // 10) * 10

for i in range(0, size + 1, 10) :
    print(n[i:i + 10])