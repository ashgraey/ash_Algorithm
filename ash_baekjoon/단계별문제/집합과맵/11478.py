'''
문제 서로 다른 문자열의 개수//
'''
import sys
input = sys.stdin.readline

n = input().strip()
size = len(n) # 5
arr = set()

for i in range(size) :
    for j in range(i, size) :
        temp = n[i:j+1] # 이게 핵심
        # a ab aba abab ababc
        # b ba bab babc 
        # a ab abc
        # b bc
        # c
        # print(temp)
        arr.add(temp)

print(len(arr)) 
 
