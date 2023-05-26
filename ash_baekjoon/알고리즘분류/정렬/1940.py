'''
문제 주몽//

알고리즘//
정렬, 두포인터

키포인트//
두개의 합이 갑옷을 만들기 위한 값! => 2차 반복으로 시도

review//
일단 나는 정렬을 쓰지 않음 경우의 수가 2가지여서 2차 반복으로 2가지의 경우의 수의 합이 재료가 되는것 모든것을 구하려함.
브루트포스에 가깝게 구했다.
다른 사람들 풀이를 보면 완벽히 이해하지는 못했지만 일단 정렬을 시켜 가장 작은수와 큰수를 더함 값의 크기의 결과에 따라 가장 작은값을 올리거나 큰값을
내리는 조건문을 건다.
기본적으로 반복문을 하나만 사용했기때문에 효율성이 훨씬 좋다. 기존의 익숙한 풀이 방식으로 풀었고 정답이긴 하지만 내가 짠 코드는 효율성 부분에서 떨어지는거 같다.
'''

import sys
input = sys.stdin.readline

size = int(input())
armor = int(input())
material = list(map(int, input().split()))

# print(material)
cnt = 0 
for i in range(size - 1) :

    for j in range(i, size) :
        if i != j and material[i] + material[j] == armor :
            cnt += 1 

print(cnt)

# 백준 다른 사람 코드
# import sys
# input = sys.stdin.readline
# n = int(input())
# m = int(input())
# A = list(map(int, input().split()))
# A.sort()

# i = 0
# j = n-1
# count = 0

# while i < j:
#     if A[i] + A[j] < m:
#         i += 1
#     elif A[i] + A[j] > m:
#         j -= 1
#     else:
#         i += 1
#         j -= 1
#         count += 1

# print(count)