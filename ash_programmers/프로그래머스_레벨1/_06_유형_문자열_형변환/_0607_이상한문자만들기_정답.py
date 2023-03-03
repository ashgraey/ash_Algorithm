# https://school.programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    # 공백으로 split
    answer = ''
    a = s.split(" ")
    print(a)


    main = ""
    for i in range(len(a)):
        temp = ""
        for j in range(len(a[i])):
            if j % 2 == 0:
                temp += a[i][j].upper()
            else:
                temp += a[i][j].lower()
        main += temp
        main += " "
        
    # 마지막 공백 자르기
    answer = main[:-1]
    # answer = main
    return answer

s = "try hello world"
a = solution(s)
print(a)