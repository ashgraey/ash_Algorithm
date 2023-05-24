'''
문제 베스트셀러//

알고리즘//
정렬, 자료구조, 문자열, 해시를 이용한 집합과 맵

키포인트//
딕셔너리의 숙련도
'''
# key에 초기값이 없는데 값(value)를 증가시키고 싶다면 dict.get("키", 초기값) 메서드를 쓰면된다.
# myDict = {}

# for _ in range(10) :
#     myDict["A"] = myDict.get("A", 0) + 1

# print(myDict)

import sys
input = sys.stdin.readline

n = int(input())

bookDict = {}
for _ in range(n) :
    key = input().rstrip()
    bookDict[key] = bookDict.get(key, 0) + 1

# lambda를 사용하여 value는 내림차순, key는 사전순이니 오름차순
bookDict = dict(sorted(bookDict.items(), key=lambda x : (-x[1], x[0])))

# 첫번째 key의 값이 가장 많이 팔린 책의 이름, 첫번째 key값을 가져오는 메서드 next(), iter()
firKey = next(iter(bookDict))
print(firKey)