'''
문제 거스름돈//
'''
import sys
input = sys.stdin.readline

n = int(input())
# arr = [5, 2]

# 거스름돈 5보다 크거나 같고 거스름돈이 홀수라면
cnt = 0
ck = False
while n > 0 :
    if n >= 9 :
        n -= 5 
        cnt += 1 
    
    elif n % 2 == 1 and n >= 5 : 
        while n > 0 :
            n -= 5
            cnt += 1
    elif n % 2 == 0 and n >= 2 :
        while n > 0 :
            n -= 2
            cnt += 1
    
    else : 
        # answer = -1
        ck = True
        break

if ck : 
    print(-1)
else : 
    print(cnt)

# 안지선이 답 // 뭔가 깔끔ㅋㅋ
# change = int(input())
# count = 0

# while True:
#     if change%5 == 0:
#         count += change//5
#         break
#     else:
#         change -= 2
#         count += 1

#     if change < 0:
#         break

# if change < 0:
#     print(-1)
# else:
#     print(count)


