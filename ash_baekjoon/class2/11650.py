'''
문제
2차원 평면 위의 점 N개가 주어진다. 
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. 
(-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
'''

import sys
n = int(sys.stdin.readline())

# nList = [map(sys.stdin.readline().split()) for _ in range(n)]
# print(nList)

# # 정수형으로 받기
# nList = []
# for _ in range(n) :
#     temp = sys.stdin.readline().split()
#     temp[0] = int(temp[0])
#     temp[1] = int(temp[1])
#     nList.append(temp)

nList = []
for _ in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    nList.append([a, b])

# print(nList)

nList.sort() # y좌표 기준 오름차순 정렬

for i in range(len(nList)) :
    print(nList[i][0], nList[i][1])

# for i in range(len(nList)) :
    
#     min = nList[i][-1]
#     minIdx = i
#     for j in range(i, len(nList)) :
#         if min > nList[j][-1] :
#             min = nList[j][-1]
#             minIdx = j
    
#     temp2 = nList[i]
#     nList[i] = nList[minIdx]
#     nList[minIdx] = temp2
#     print(nList[i])