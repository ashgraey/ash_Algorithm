'''
문제 수 정렬하기5//

알고리즘//
정렬

키포인트//
일단 sort()로 해보자
'''
import sys
input = sys.stdin.readline

n = int(input())
nList = [int(input()) for _ in range(n)]

nList.sort()
# print(nList)
for v in nList :
    print(v)