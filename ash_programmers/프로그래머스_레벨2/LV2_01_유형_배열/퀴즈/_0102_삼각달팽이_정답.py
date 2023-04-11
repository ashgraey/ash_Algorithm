# https://school.programmers.co.kr/learn/courses/30/lessons/68645

# 삼각달팽이의 모양을 0으로 초기화
def getTriangle(n):
    arr = []
    for i in range(n):
        temp = [0 for i in range(i + 1)]
        arr.append(temp)
    return arr

# 삼각달팽이 요소의 total
def getCount(n):
    total = 0
    for i in range(n):
        total += (i + 1)
    return total

def solution(n):
    arr = getTriangle(n)
    total = getCount(n)
    #print(arr)
    #print(total)

    # dir은 방향, down, up, right
    dir = "d"
    # y,x 좌표값
    y = 0
    x = 0
    # c 카운트
    c = 0
    mx = n
    i = 1
    answer = []
    while True:
        if i > total:
            break

        c += 1
        if mx == c:
            if dir == "d":
                dir = "r"
            elif dir == "r":
                dir = "u"
            elif dir == "u":
                dir = "d"
            mx = mx - 1
            c = 0 
            
        arr[y][x] = i
        if dir == "d":
            y += 1
        elif dir =="r":
            x += 1
        elif dir == "u":
            y -= 1
            x -= 1   
        i += 1
    # 0으로 초기화한 arr을 값을 찾아 넣는다. 최종적으로 2차원배열 모양으로 만들어놓아야함    
    for i in arr :
        print(i)
    
    # answer에 값을 하나씩 넣는다. 일차원 리스트로 변환
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            answer.append(arr[i][j])

    return answer 

n = 6
result = solution(n)
print(result)