# https://school.programmers.co.kr/learn/courses/30/lessons/12977
'''
문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

입출력 예
nums	    result
[1,2,3,4]	1
[1,2,7,6,4]	4

'''

import math
import itertools

def prime_num(num) :
    # 소수 구하는 로직
    for i in range(2, int(math.sqrt(num)) + 1) :
        # 받은값이 i로 나누어지면 소수가 아님, return False
        if num % i == 0 :
            return False
    return True
# itertools 라이브러리의 itertools.combinations() 함수는 입력받은 배열의 경우의 수를 찾는 함수입니다.
# 여기서 중요한 것은 combinations는 순열과 조합에서 조합을 뜻하는 것으로 순서를 중요시하지 않는 것이 특징입니다
def solution(nums):
    cnt = 0
    primeNumList = []
    for i in itertools.combinations(nums, 3) :
        primeNumList.append(sum(i))
        # print(num)
    for i in primeNumList :
        if prime_num(i) :
            cnt += 1 
        # else :
        #     continue

    return cnt

    

nums = 	[1, 2, 7, 6, 4]
result = solution(nums)
print(result)