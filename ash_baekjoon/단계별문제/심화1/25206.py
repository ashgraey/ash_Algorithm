'''
전공평점은 전공과목별 (학점 * 과목평점)의 합을 학점의 총합으로 나눈 값
'''

mark = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F", "P"]
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0, 0.0]

# 입력 : 과목명 학점 등급

# 20줄에 걸쳐서 입력을 받는다
total = 0
totalGrade = 0
for _ in range(20) :
    gradeList = list(input().split())
    # print(gradeList)

    
    for i in range(len(mark)) :
        if gradeList[-1] == mark[i] : 
            markIdx = i
            break
         
    
    # print(float(gradeList[1]))
    # print(grade[markIdx])

    # (학점 * 과목평점)의 합
    # 실수 형변환을 float으로 해야하는데 int로 시킴
    if gradeList[-1] != "P" :
        total += float(gradeList[1]) * grade[markIdx]
        # 학점의 총합
        totalGrade += float(gradeList[1])

# 출력 : 전공 평점
answer = total / totalGrade
result = format(answer,'.6f')
print(result)