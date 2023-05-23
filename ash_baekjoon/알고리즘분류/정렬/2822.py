'''
문제 점수 계산//

알고리즘//
정렬

키포인트//
1. 내림차순 정렬 -> 앞에서부터 5개 점수를 빼내고 인덱스 + 1한 값을 출력한다.
'''

import sys
input = sys.stdin.readline

scoreList = [int(input()) for _ in range(8)]
sorted_scoreList = sorted(scoreList, reverse = True)
# print(sorted_scoreList)

total = 0
lankList = []
for i in range(5) :
    total += sorted_scoreList[i]
    lankList.append(scoreList.index(sorted_scoreList[i]) + 1)


lankList.sort()

print(total)
for v in lankList :
    print(v, end = " ")
