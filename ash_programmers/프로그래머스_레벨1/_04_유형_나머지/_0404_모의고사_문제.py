# https://school.programmers.co.kr/learn/courses/30/lessons/42840
'''
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 
수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
'''

def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0, 0, 0]
    for i in range(len(answers)) :
        # 만약 answers가 더 길고 a,b,c가 짧을 경우 i로만 비교하면 index out of range 오류가 난다.
        # 왜냐면 반복의 기준이 answers의 길이이기 때문에
        # 이 경우 i % len(a)를 쓰면 out of range가 안나고 길이를 넘을 경우 다시 맨 앞으로 돌아가 비교한다.
        # 항상 짤 때 길이를 잘 생각해야함
        
        if answers[i] == a[i % len(a)] :
            count[0] += 1
        if answers[i] == b[i % len(b)] :
            count[1] += 1 
        if answers[i] == c[i % len(c)] :
            count[2] += 1

    print(count)
    cntMax = max(count)

    for i in range(3) :
        if cntMax == count[i] :
            answer.append(i + 1)
    answer.sort()
    
    return answer


# answers =  [5, 5, 4, 2, 3] 
answers =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# answers =  [1, 3, 2, 4, 2] 
result = solution(answers)
print(result)