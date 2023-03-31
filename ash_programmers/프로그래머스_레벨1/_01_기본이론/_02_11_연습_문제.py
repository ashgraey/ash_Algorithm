"""
[문제]
    아래 itemData 아이템들의 총목록이다.
    salesData 는 오늘의 매출 현황이다. 
    상품이름과 판매개수가 한쌍이다.
    오늘의 총매출 결과를 출력하시오.
    단 판매개수로 내림차순하시오.
[예시]
    감자깡 13
    새우깡 9
    콘칩 3
    오징어볼 0
"""
itemData = ["새우깡", "감자깡", "오징어볼", "콘칩"]
salesData = "새우깡 5,감자깡 6,새우깡 4,콘칩 3,감자깡 7"
viewData = {}

# 3/31 한번 더 풀어보자
salesData = salesData.split(",")

salesDataList = []
for i in range(len(salesData)) :
    token = salesData[i].split()
    salesDataList.append(token)

# print(salesDataList)

itemDict = {}
for i in itemData :
    itemDict[i] = 0

# print(itemDict)

for i in itemData : 

    for j in range(len(salesDataList)) :
        salesData = salesDataList[j]
        if i == salesData[0] :
            itemDict[i] += int(salesData[1]) 

# print(itemDict)

# value를 기준으로 내림차순 정렬
itemDict = sorted(itemDict.items(), key=lambda x : x[1], reverse=True)
# print(itemDict)
for i in itemDict :
    print(i)


# sale = salesData.split(",")
# saleList = []
# for i in range(len(sale)):
#     saleList.append(sale[i].split(" "))

# print(saleList)
# # 아이템 이름 먼저 복사
# for key in itemData:
#     viewData[key] = 0
# print(viewData)

# # 딕셔너리로 모으기
# for key in viewData.keys():
#     for j in range(len(saleList)):
#         if key == saleList[j][0]:
#             viewData[key] += int(saleList[j][1])

# print(viewData)
# print()
# sortedItem = sorted(viewData.items(), key=lambda x: x[1], reverse=True)
# for i in sortedItem:
#     print(i)
