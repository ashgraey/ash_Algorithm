'''
문제 A -> B//

알고리즘//
그리디
그래프
그래프탐색
너비우선탐색

키워드//
역순으로 가보자
'''
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

cnt = 0
while True :
    if b % 10 == 1 :
        b //= 10
        cnt += 1 
    elif b % 2 == 0 :
        b //= 2 
        cnt += 1
    
    if b == a :
        print(cnt + 1)
        break
    elif (b % 2 != 0) and (b % 10 != 1) or b < a :
        print(-1)
        break

# if int(b) == a : 
#     print(cnt + 1)
# else :
#     print(-1)