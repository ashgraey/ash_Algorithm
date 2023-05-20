'''
문제 세 수//

알고리즘 //
정렬, 구현

키포인트//
1) sort()쓰면 안될라나?

'''

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

arr = [a, b, c]
arr.sort()
print(arr[1])