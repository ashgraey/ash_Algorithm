'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
'''
import sys
n = int(sys.stdin.readline())

nList = list(map(int, sys.stdin.readline().split()))
# nList = [int(sys.stdin.readline()) for _ in range(n)]

scList = []
maxCnt = 0
for i in range(len(nList)) :
    cnt = 1 
    # idx = i 
    for j in range(i, len(nList)) :
        if nList[i] < nList[j] :
            i = j
            cnt += 1 

    if maxCnt < cnt :
        maxCnt = cnt

# print(scList)
# max = max(scList) 
# print(max)
print(maxCnt)

# nList = list(set(nList))
# print(nList)
# min = nList.index(min(nList))
# # print(min)

# cnt = 1
# for i in range(min, len(nList)) :
#     if nList[min] < nList[i] :
#         min = i
#         cnt += 1 
# print(cnt)
# max = nList.index(max(nList))
# print(max)
# for i in nList :
