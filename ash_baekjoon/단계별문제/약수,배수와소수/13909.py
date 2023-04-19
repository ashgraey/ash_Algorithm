'''
문제 창문 닫기//
'''
# 규칙성을 찾는 문제// 답을 출력하다보면 입력값  n의 제곱근의 정수형 값이 정답이다.
# 이런 문제도 있구먼..
import sys,math
input = sys.stdin.readline

n = int(input())
print(int(math.sqrt(n)))

# 메모리초과// 입력값의 제한이 너무 커서 배열로 받으면 안됨
# import sys
# input = sys.stdin.readline

# n = int(input())
# window_list = [0] * n

# for i in range(n) :

#     for j in range(i, n, i + 1) :
#         if window_list[j] == 0 :
#             window_list[j] = 1 
#         elif window_list[j] == 1 :
#             window_list[j] = 0 

# cnt = 0 
# for window in window_list :
#     if window == 1 :
#         cnt += 1
# print(window_list)
# print(cnt)