'''
문제 접미사 배열//

알고리즘//
문자열, 구현

키포인트//
'''
import sys
input = sys.stdin.readline

word = input().rstrip()

arr = []
for i in range(len(word)) :
    arr.append(word[i:])

arr = sorted(arr)
for v in arr :
    print(v)


