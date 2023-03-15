'''
문제 직각삼각형//
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

입력
입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 
각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.

출력
각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.
'''
import sys 

while True :
    total = 0
    maxTotal = 0 
    numList = list(map(int, sys.stdin.readline().split()))
    # numList = [int(sys.stdin.readline().split())]

    if numList[0] == 0 and numList[1] == 0 and numList[-1] == 0 :
        break
   
    maxIdx = numList.index(max(numList))
    
    for i in numList :
        if numList[maxIdx] != i :
            total += (i * i)

    maxTotal = (numList[maxIdx] * numList[maxIdx])
    
    # print(total, maxTotal)
    if maxTotal == total :
        print("right")
    else :
        print("wrong")
    


    

