'''

'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def solution(n) :
    arr = []
    for _ in range(n) :
        aList = list(map(int, input().split()))
        arr.append(aList)
    # for i in aList :

    return arr

a = solution(n)
b = solution(n)

for i in range(len(a)) :
    for j in range(len(a[i])) :
        print(a[i][j] + b[i][j], end = " ")
    print()
# for i in range(len(answer)) :
#     for j in range(len(answer[i])) :
#         print(answer[i][j], end = " ")
#     print()