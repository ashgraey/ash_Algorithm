# https://school.programmers.co.kr/learn/courses/30/lessons/12919
def solution(seoul):
    answer = ''
    for i in range(len(seoul)) :
        if seoul[i] == "Kim" :
            answer =  "김서방은 " + str(i) + "에 있다"

    return answer

s = ["Jane" , "Kim"]
a = solution(s)
print(a)

'''
def solution(seoul):
    answer = ''
    idx = 0 
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            idx += 1 
            answer = "김서방은 " + str(i) + "에 있다"

s = ["Jane" , "Kim"]

a = solution(s)
print(a)

=> idx변수 때문에 자꾸 시간초과났음
테스트가 통과되지 않았음
불필요한 변수는 굳이 안 들어가는게 좋다.
'''
