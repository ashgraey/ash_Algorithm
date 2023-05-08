'''
문제 명령 프롬프트//

알고리즘//
구현
문자열

키포인트//
'''
import sys
input = sys.stdin.readline

n = int(input())

nList = [input().rstrip() for _ in range(n)]
# print(nList)

if len(nList) == 1 :
    print(nList[0])

else :
    for i in range(len(nList) - 1) :
        temp = ""
        for j in range(len(nList[i])) :
            if nList[i][j] != nList[i + 1][j] :
                temp += "?"
            else :
                temp += nList[i][j]

        nList[i + 1] = temp
        # print(nList[i])
    print(temp)

