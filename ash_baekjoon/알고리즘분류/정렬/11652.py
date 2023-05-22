'''
문제 카드//

알고리즘//
정렬, 자료구조, 해시를 사용한 집합과 맵

키포인트//
기준 카드를 만들어 카운트 시켜보자
'''

import sys
input = sys.stdin.readline

tc = int(input())
arr_num = [int(input()) for _ in range(tc)]
# arr_set = list(set(arr_num))

# max = 0
# for v in arr_set :
#    cnt = arr_num.count(v)
#    if max < cnt :
#       max = cnt

# # print(max)
# for v in arr_num :
#    if max == arr_num.count(v) :
#       print(v)
#       break

# 딕셔너리 초기화
dict_num = {}
for v in arr_num :
    dict_num[v] = 0 

# 딕셔너리에 value 증가
for k in dict_num :
    for v in arr_num :
        if k == v :
            dict_num[k] += 1

# 카운트가 동일한 경우 작은 값을 우선으로 뽑기 위해 정렬
dict_num = dict(sorted(dict_num.items()))   
# print(dict_num)

dict_max = max(dict_num.values())
# print(dict_max)

for k in dict_num :
    if dict_num[k] == dict_max :
        print(k)
        break