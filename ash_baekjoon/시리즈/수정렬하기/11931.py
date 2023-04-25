'''
문제 수정렬하기//
'''
import sys
input = sys.stdin.readline

n = int(input())

n_list = []
for _ in range(n) :
    n_list.append(int(input()))

n_list = sorted(n_list, reverse=True)
for n in n_list :
    print(n)