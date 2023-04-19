'''
문제 문자열 집합//
'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr_n = set()
for _ in range(n) :
    arr_n.add(input().rstrip())


cnt = 0
for i in range(m) :
    word_m = input().rstrip()

    if word_m in arr_n : 
        # print(":", word_m)
        cnt += 1
    
print(cnt)