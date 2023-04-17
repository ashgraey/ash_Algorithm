'''
문제 진법변환2//

10진수를 N진수로 바꾸어 출력하자
'''

import sys 
input = sys.stdin.readline

n, b = map(int, input().split())

result = 1
while True :
    if n < result : 
        break 

    result *= b

print(result)