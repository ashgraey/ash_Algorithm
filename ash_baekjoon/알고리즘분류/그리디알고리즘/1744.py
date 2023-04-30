'''
문제 수묶기//

알고리즘//
그리디
정렬

키워드//
하나씩 생각해보면 된다. 
양수, 음수, 1을 나눠서 생각하면 편하다.
'''
import sys
input = sys.stdin.readline

n = int(input())

# 양수, 음수(0포함), 1의 따로 받는다.
min_arr = []
pls_arr = []
one = []

for i in range(n) :
    num = int(input())

    if num > 1 :
        pls_arr.append(num)

    elif num <= 0 :
        min_arr.append(num)

    elif num == 1 :
        one.append(num)


# 정렬
# 양수는 큰수끼리 묶었을때 크니깐 내림차순
# 음수는 작은수끼리 묶었을때 크니깐 오름차순으로 정렬한다. 
pls_arr = sorted(pls_arr, reverse=True)
min_arr = sorted(min_arr)
# print(pls_arr, min_arr) 

# 1은 곱하는거보다 더하는게 이득이니깐 더해준다. 
total_one= sum(one)

#조건에 맞게 묶는다. 
# 양수
total_p = 0
if len(pls_arr) % 2 == 0 : # 짝수
    for i in range(0, len(pls_arr), 2) : # 2개씩 묶어서
        total_p += (pls_arr[i] * pls_arr[i + 1])
        # print(total_p)

else : # 홀수면 가장 작은 수만 안 묶고 더 해줌
    for i in range(0, len(pls_arr) - 1, 2) :
        total_p += (pls_arr[i] * pls_arr[i + 1])
    total_p += pls_arr[-1]

# 음수
total_m = 0
if len(min_arr) % 2 == 0 :
    for i in range(0, len(min_arr), 2) :
        total_m += (min_arr[i] * min_arr[i + 1])
else :
    for i in range(0, len(min_arr) - 1, 2) :
        total_m += (min_arr[i] * min_arr[i + 1])
    total_m += min_arr[-1]


# print(total_one, total_p, total_m)
print(total_one + total_p + total_m)