'''
문제 세수 정렬//

알고리즘//
정렬

키포인트//
정렬gi
'''

import sys
input = sys.stdin.readline

three_num = list(map(int, input().split()))
three_num.sort()
for v in three_num :
    print(v, end = " ")