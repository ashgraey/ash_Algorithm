'''
문제 포켓몬 마스터 이다솜//
'''

import sys
input = sys.stdin.readline

num = "0123456789"
n, m = map(int, input().split())
size = n + m

arr_poke = {}
for i in range(1, size + 1) :
    arr_poke[str(i)] = input().strip()

    # if i > n : 
        
# print(arr_poke)


for _ in range(m) :
    find = input().strip()
    # print(find)

    if find.isdigit() :
        print(arr_poke[find])
    
    # else :
    #     print(arr_poke[arr_poke.get(find)])
       
