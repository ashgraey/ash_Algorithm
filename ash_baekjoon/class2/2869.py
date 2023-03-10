'''
문제
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

출력
첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.
'''
import sys 
import math

A, B, V = map(int, sys.stdin.readline().split())

# 반복문을 사용하면 시간초과에 걸림
# 수학적으로 접근해야한다.

# day = 0
# count = 0
# while True :
#     count += A
#     if count >= V : 
#         day += 1 
#         break
#     else :
#         count -= B
    
#     day += 1
# print(day)

# day = 0
# count = 0  
# while V > count :
#     count += A
#     if count < V : 
#         count -= B
#     day += 1 
# print(day)

day = (V - B) / (A - B)
print(math.ceil(day)) # 소수가 나올 수 있으므로 반올림 해준다.