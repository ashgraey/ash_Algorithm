'''
문제 숫자카드2//
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
상근이는 숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 
이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 
각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
nList = [*map(int, input().split())]
m = int(input())
mList = [*map(int, input().split())]

# print(nList)
# print(mList)

# nList의 중복값을 딕셔너리에 저장
dict = {}
for i in nList :
    if i in dict :
        dict[i] += 1 
    else :
        dict[i] = 1

# print(dict)
for i in mList :
    result = dict.get(i)
    if result == None :
        print(0, end = " ")
    else :
        print(result, end = " ")


# # 이분탐색으로만 풀면 시간초과
# n = int(sys.stdin.readline())
# # n = 10
# nList = sorted(list(map(int, sys.stdin.readline().split())))
# # nList = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
# # # 상근이 카드 M 
# m = int(sys.stdin.readline())
# mList = list(map(int, sys.stdin.readline().split()))
# # mList = [10, 9, -5, 2, 3, 4, 5, -10]

# # nList.sort()
# # print(nList)

# def binary_search(arr, target, start, end) :
#     while start <= end : 
#         mid = (start + end) // 2

#         if arr[mid] == target : 
#             return nList.count(target)

#         elif arr[mid] < target :
#             start = mid + 1
        
#         else :
#             end = mid - 1
    
#     return 0

# for i in mList :
#     print(binary_search(nList, i, 0, n - 1), end = " ")

# # count함수를 썼지만 시간초과 ㅜㅜ
# # 제시되는 숫자 카드 N
# n = int(sys.stdin.readline())
# nList = list(map(int, sys.stdin.readline().split()))
# # nList = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
# # 상근이 카드 M 
# m = int(sys.stdin.readline())
# mList = list(map(int, sys.stdin.readline().split()))
# # mList = [10, 9, -5, 2, 3, 4, 5, -10]

# # print(set(nList))
# for i in mList :
#     if i in nList :
#         print(nList.count(i), end = " ")
#     else :
#         print(0, end = " ")

# start = 1 
# end = 
# cntList = []
# for i in mList :
#     cnt = 0 
#     if i in nList :
#         idx = nList.index(i)
    
#     temp = set(nList[idx])
#     print(temp)
    
# for i in cntList :
#     print(i, end = " ")