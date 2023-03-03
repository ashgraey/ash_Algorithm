# # https://school.programmers.co.kr/learn/courses/30/lessons/86051
'''
굳이 중복이 있는지 없는지 확인을 하지 않아도 됨 
'''
def solution(numbers):
    # 1 ~ 10까지 total을 구한다
    total = 0
    for i in range(10):
        total += i

    # a리스트의 합계를 구한다. 
    a = sum(numbers)
    # total - a
    b = total - a
    return b
numbers = [1,2,3,4,6,7,8,0]

result = solution(numbers)
print(result)