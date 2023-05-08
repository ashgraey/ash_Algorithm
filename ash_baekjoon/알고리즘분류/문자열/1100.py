'''
문제 하얀칸//

알고리즘//
문자열
구현

'''
import sys
input = sys.stdin.readline

chessPan = []
for _ in range(8) :
    chessPan.append(input().rstrip())

# print(chessPan)
cnt = 0
for i in range(len(chessPan)) : 
    for j in range(len(chessPan[i])) :
        if i % 2 == 0 :
            if j % 2 == 0 and chessPan[i][j] == "F" :
                cnt += 1 
        else :
            if j % 2 == 1 and chessPan[i][j] == "F" : 
                cnt += 1 
            

print(cnt)
