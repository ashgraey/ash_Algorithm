'''
문제 구간 합 구하기//
'''
# 시간초과 for 한번만 써야한는 듯
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())

# arr_n = list(map(int, input().split()))


# for _ in range(m) :
#     i, j = map(int, input().split())

#     total = 0 
#     for k in range(i - 1, j) :
#         total += arr_n[k]
    
#     print(total)

# splice로 잘라서 sum을 통합 합을 구하는 것도 시간초과
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())

# arr_n = list(map(int, input().split()))

# for _ in range(m) :
#     i, j = map(int, input().split())
#     print(sum(arr_n[i-1:j]))

# chat GPT// 누적합을 통해서 구간합을 구해줘야 함
# [5, 4, 3, 2, 1]
import sys
input = sys.stdin.readline
N, M = map(int, input().split())  # 수의 개수 N, 합을 구해야 하는 횟수 M 입력받기
nums = list(map(int, input().split()))  # N개의 수 입력받기
prefix_sum = [0]  # 누적 합을 저장할 리스트 초기화
# print(prefix_sum)

# 누적 합 구하기
for i in range(N):
    prefix_sum.append(prefix_sum[i] + nums[i]) # 이게 생각하기 어려운듯, 누적 합을 구하는게
    # print(prefix_sum)

# 구간 합 구하기
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1]) # i값은 시작값이니깐 i-1인 이전의 합까지만 제거해주면 구간의 합을 구할 수 있다
