'''
문제 중복 빼고 정렬하기//

알고리즘//
정렬

키포인트//
중복된 수는 제거하고 정렬
1차 시도) set() 메서드를 이용해서 중복을 제거하고 출력 => 중복을 제거하고 자동으로 정렬을 시켜준다고 생각 => 틀렸습니다. 
2차 시도) set() 메서드를 이용해 중복을 제거하고 다시 sort()로 정렬을 시키고 출력 => 정답
'''

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

n_list = list(set(n_list))
n_list.sort()
# for v in n_list :
#     print(v, end = " ")
print(*n_list) # 반복문 없이 배열을 요소를 출력하는 방법