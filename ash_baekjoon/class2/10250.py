'''
ACM호텔 문제//
'''

import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    h, w, n = map(int, input().split())

    
    acm = []
    for i in range(1, h + 1) :
        num = 100
        temp = []
        num *= i
        for j in range(1, w + 1) : 
            num += 1 
            temp.append(num)
        acm.append(temp)

    cnt = 0
    for i in range(w) :
        for j in range(h) :
            cnt += 1 
            if cnt == n :
                # print(j,i)
                print(acm[j][i])



# print(acm)
# for i in acm :
#     print(i)
        

