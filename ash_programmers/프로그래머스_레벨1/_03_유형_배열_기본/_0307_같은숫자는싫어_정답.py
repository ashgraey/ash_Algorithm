# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    a = arr[0]
    answer.append(a)
    for i in range(len(arr) - 1):
        # 변수 a의 원소를 저장 중복되지 않는 원소가 나올때마다 원소의 값을 교체
        # 0 인덱스에 값을 넣고 시작하였기 때문에 i + 1 == 인덱스 1부터 시작
        if a != arr[i + 1]:
            a = arr[i + 1]
            answer.append(a)
    return answer
arr = [1,1,3,3,0,1,1]
a = solution(arr)
print(a)

# 변경 후
def solution(arr):
    answer = []
    a = arr[0]
    answer.append(a)
    for i in range(1, len(arr)):
        # 변수 a의 원소를 저장 중복되지 않는 원소가 나올때마다 원소의 값을 교체
        # 0 인덱스에 값을 넣고 시작하였기 때문에 i + 1 == 인덱스 1부터 시작
        # 가독성이 떨어지는거 같아 i를 1부터 돌림
        if a != arr[i]:
            a = arr[i]
            answer.append(a)
    return answer
arr = [1,1,3,3,0,1,1]
a = solution(arr)
print(a)