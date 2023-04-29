'''
문제 거스름돈//
'''
import sys
input = sys.stdin.readline

pay = int(input())
pay = 1000 - pay

change = [500, 100, 50, 10, 5, 1]
# print(pay)
i = 0 
cnt = 0
while pay > 0 : 
    if pay >= change[i] :
        pay -= change[i]
        cnt += 1
    
    else : 
       i += 1 
    
    # print(pay)

print(cnt)
    
