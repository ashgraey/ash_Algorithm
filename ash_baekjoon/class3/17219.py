'''
문제 비밀번호 찾기//
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}
find = []
for i in range(n + m) :

    if i >= n :
        find.append(input().strip())
        # print(dict[find])
    else :
        user = input().strip()
        user = user.split(" ")
        dict[user[0]] = user[1]

# print(find)    
for i in find :
    print(dict[i])
# for _ in range(m) :
#     find = input().strip()
#     print(dict[find])