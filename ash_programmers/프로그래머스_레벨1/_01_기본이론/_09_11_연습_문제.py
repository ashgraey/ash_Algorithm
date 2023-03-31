"""
    [문제]
        num1 과 num2 에 랜덤으로 (0~9) 사이의 숫자를 저장후 두수자간의 거리를 출력하시오.
        가로 세로 각각의 이동은 1칸으로 간주하다.
        대각선으로 계산할수는없다. 
    [예시]
        num1 = 1 , num2 = 3 이면 1과 3사이의 거리는 가로로 2이며, 정답은 2이다. 

        num1 = 7 , num2 = 3 이면 7과 3사이의 거리는 가로로 2 + 세로로 2 정답은 4이다. 

        둘이 같은수이면 정답은 0이다. 
"""
import random

a = [   
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [-1,0,-1]]

# y,x 좌표값 
# 1 : 0, 0
# 3 : 0, 2

# 7 : 2, 0
# 3 : 0, 2


def check(n1, n2) :
    if n1 == n2 :
        return 0
    
    for i in range(len(a)) :
        for j in range(len(a[i])) :
            if a[i][j] == n1 :
                n1_y = i
                n1_x = j
            
            if a[i][j] == n2 :
                n2_y = i
                n2_x = j
        
    # print(n1_y, n1_x)
    # print(n2_y, n2_x)
    y = n1_y - n2_y
    x = n1_x - n2_x
    if y < 0 :
        y = -y
    if x < 0 :
        x = -x

    return y + x

    

num1 = 0
num2 = 0

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
print(num1, num2)
# num1 = 1
# num2 = 1
answer = check(num1, num2)
print(answer)
