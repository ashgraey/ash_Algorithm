'''
문제 팩토리얼 0의 개수//
'''

import sys
input = sys.stdin.readline

n = int(input())

result = 1
for i in range(1, n + 1) :
    result *= i 
    # print(result)

# print(str(result))
result = str(result)
# print(result)
# result = sorted(reverse=True)
# print(result)
# for i in range(len(result)) :

cnt = 0
i = len(result) - 1
while i > 0 : 
    if result[i] == "0" : 
        cnt += 1
    else : 
        break
    i -= 1

print(cnt)