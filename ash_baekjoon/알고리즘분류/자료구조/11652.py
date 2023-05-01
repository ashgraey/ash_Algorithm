'''
문제 카드//

알고리즘//
자료구조
정렬
해시 

키워드//
'''
import sys
input = sys.stdin.readline

n = int(input())

dict = {}
for _ in range(n) :
    key = int(input())
    dict[key] += 1

print(dict)