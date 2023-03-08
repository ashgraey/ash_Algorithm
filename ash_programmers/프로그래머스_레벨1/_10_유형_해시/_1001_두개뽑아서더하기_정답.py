# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    myset = set() # 이건 생각 못했음ㅋㅋ
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                a = numbers[i] + numbers[j]
                myset.add(a)

    # print(myset)
    for v in myset:
        answer.append(v)
    answer.sort()
    # print(answer)
    return answer

numbers = [2,1,3,4,1]
result = solution(numbers)
print(result)

