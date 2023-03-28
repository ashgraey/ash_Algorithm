'''
문제 수정렬하기//
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''


# sort()쓰면 메모리 초과
# 원래쓰는 정렬방식도 메모리 초과
# import sys 
# n = int(sys.stdin.readline())

# nList = [int(sys.stdin.readline()) for _ in range(n)]

# for i in range(len(nList)) :
#     min = nList[i]
#     minIdx = i
#     for j in range(i,len(nList)) :
#         if min > nList[j] :
#             min = nList[j]
#             minIdx = j 
    
#     temp = nList[i]
#     nList[i] = nList[minIdx]
#     nList[minIdx] = temp
# print(nList)



