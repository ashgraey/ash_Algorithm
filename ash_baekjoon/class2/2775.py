'''
문제
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.

이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.

아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 
주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 
단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

입력
첫 번째 줄에 Test case의 수 T가 주어진다. 
그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

출력
각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.
'''
# k : 층, n : 호

# import sys
# input = sys.stdin.readline

tc = int(input())

# answer = []
for _ in range(tc) :
    # aptList = [
    # [1, 2, 3]
    #        ]
    
    # idxList = [int(input()) for _ in range(2)]

    # k = idxList[0]
    # n = idxList[1]

    k = int(input())
    n = int(input())
    aptList = [[x for x in range(1, n + 1)]]
    # print(aptList)

    # print(aptList[0][0])
    for i in range(k) :
        temp = []
        for j in range(n) :
            total = 0
            for l in range(j+1) :
                total += aptList[i][l]
                # print(i, j)
            temp.append(total)
        aptList.append(temp)

    # answer.append(aptList[k][n - 1])
    print(aptList[k][n - 1])



# import sys

# testCase = int(sys.stdin.readline())
# for _ in range(testCase) :
#     a, b = map(int, sys.stdin.readline())

#     apt = []
#     for i in range(a + 1) :
#         temp = []
#         for j in range(b) :
#             temp.append(j + 1)
        
#         apt.append(temp)

# 인터넷 풀이
# t = int(input())

# for _ in range(t):  
#     floor = int(input())  # 층
#     num = int(input())  # 호
#     f0 = [x for x in range(1, num+1)]  # 0층 리스트
#     for k in range(floor):  # 층 수 만큼 반복
#         for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
#             f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
#     print(f0[-1])  # 가장 마지막 수 출력