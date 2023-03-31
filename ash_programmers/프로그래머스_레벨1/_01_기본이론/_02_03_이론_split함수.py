"""
[1] split() 함수는 문자열을 구분자로 전부 나눠서 리스트로 만들어준다.
"""
st = "김철수,이만수,김민주"
token = st.split(",")
print(token)

# 실험1 : split에 인자를 주지 않으면 공백을 기준으로 list로 나눌 것인가?
# 정답 : 공백(스페이스바)를 기준으로 나눈다
st = "안성현 안정민 안성준"
token = st.split()
print(token)

"""
[2] salesData 를 이차원 리스트로 만드시오.
"""
salesData = "새우깡 5,감자깡 6,새우깡 4,콘칩 3,감자깡 7"
tokenList = salesData.split(",")
viewList = []
for i in range(len(tokenList)):
    token = tokenList[i].split()
    viewList.append(token)
print(viewList)

# temp = salesData.split(",")
# print(temp)
# tempList = []
# for i in range(len(temp)):
#     tempList.append(temp[i].split(" "))

# for i in range(len(tempList)):
#     print(tempList[i])
