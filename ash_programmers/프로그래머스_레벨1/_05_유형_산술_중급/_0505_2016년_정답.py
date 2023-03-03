# https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    mon = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = 0
    for i in range(a - 1):
        day += mon[i] # 입력받은 달의 -1 달까지 모든 달의 날짜를 day에 합산
    day += b - 1 # -1? 
    print("day : " , day)
    index = (day + 5) % 7 # 1월 1일이 금요일이므로 day +5를 해줘야한다.   
    # print(index)
    return week[index]

a = 5
b = 24
r = solution(a , b)
print(r)