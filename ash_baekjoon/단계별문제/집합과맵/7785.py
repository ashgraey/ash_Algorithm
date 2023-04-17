'''
문제 회사에 있는 사람//
'''

import sys
input = sys.stdin.readline

n = int(input())

arr_n = {}
for i in range(n) :
    user = input().rstrip()
    user = user.split(" ")
    arr_n[user[0]] = user[1]

# print(arr_n)
result = []
for i in arr_n :
    if arr_n.get(i) == 'enter' :
        result.append(i)

result = sorted(result, reverse=True)
for i in result :
    print(i)

# dict = {}
# for i in range(len(arr_n)) :
#     # arr_n = arr_n[i]
#     dict[arr_n[i][0]] = arr_n[i][1] 
# # print(dict)
# for i in dict :
#     if dict.get(i) == 'enter' :
#         print(i)