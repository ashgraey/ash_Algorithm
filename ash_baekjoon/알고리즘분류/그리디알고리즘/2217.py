'''
문제 로프//

알고리즘//
수학
그리디
정렬

키워드//
병렬 구조일때 중량을 나눌 수 있다.
예시// 
10 15 20 25 30 35
100 / 5 + 35 
'''
import sys
input = sys.stdin.readline

n = int(input())

# arr = []
# for _ in range(n) :
#     arr.append(int(input()))

arr = [int(input()) for _ in range(n)]
# print(arr)

arr.sort()
# print(arr)

total = 0 
for i in range(len(arr) - 1) :
    total += arr[i]

# print("total : ", total)
total //= n 
print(total + arr[-1])
