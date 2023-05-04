'''
문제 k번째 수//

알고리즘//
정렬

키포인트//
1. 정렬 후 값을 출력할때에는 인덱스로 출력한다. => 같은 값을 찾으려고 반복문을 돌리면 시간초과날듯
2. 다른 사람 풀이에는 QuickSort를 많이 사용했다. => QuickSort에 대한 이해가 필요.

'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())


arrN = list(map(int, input().split()))
# print(arrN)

arrN.sort()
# print(arrN)
print(arrN[k - 1])