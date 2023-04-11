# https://school.programmers.co.kr/learn/courses/30/lessons/68645

# def get_arr(n) :
#     arr = []
#     for i in range(n) :
#         unit = [0 for i in range(i + 1) ]
#         arr.append(unit)
#     return arr

# def get_total(arr) :
#     cnt = 0
#     for i in range(len(arr)) :
#         for j in range(len(arr[i])) :
#             if arr[i][j] == 0 :
#                 cnt += 1 
#     return cnt

# def solution(n):
#     arr = get_arr(n)
#     total = get_total(arr)
#     # print(arr)
#     # print(total)

#     dir = "d"
#     x = 0
#     y = 0
#     c = 0
#     mx = n
#     i = 1 
#     while True :
#         if i > total :
#             break

#         c += 1 
#         if c == mx :
#             if dir == "d" :
#                 dir = "r"
#             elif dir == "r" :
#                 dir = "u"
#             elif dir == "u" :
#                 dir = "d"
#             mx -= 1 
#             c = 0 
        
#         arr[y][x] = i
#         if dir == "d" :
#             y += 1
#         elif dir == "r" :
#             x += 1 
#         elif dir == "u" :
#             y -= 1 
#             x -= 1
        
#         # print(arr)
#         i += 1 

#     answer = []
#     for i in range(len(arr)) :
#         for j in range(len(arr[i])) :
#             answer.append(arr[i][j])

#     return answer
        
# n = 4
# result = solution(n)
# print(result)

# chat GPT 등차수열, 출력이 이상함
# def solution(n):
#     answer = [0] * (n * (n + 1) // 2)  # 결과를 저장할 1차원 배열 생성
#     direction = 0  # 이동 방향 (0: 아래, 1: 오른쪽, 2: 위, 3: 왼쪽)
#     x, y = 0, 0  # 현재 위치 좌표
#     num = 1  # 배열에 채워질 숫자

#     for i in range(n, 0, -1):
#         if direction == 0:  # 아래로 이동
#             for j in range(i):
#                 index = x * (x + 1) // 2 + y
#                 answer[index] = num
#                 x += 1
#                 num += 1
#             x -= 1
#             y += 1
#         elif direction == 1:  # 오른쪽으로 이동
#             for j in range(i):
#                 index = x * (x + 1) // 2 + y
#                 answer[index] = num
#                 y += 1
#                 num += 1
#             x -= 1
#             y -= 1
#         elif direction == 2:  # 위로 이동
#             for j in range(i):
#                 index = x * (x + 1) // 2 + y
#                 answer[index] = num
#                 x -= 1
#                 y -= 1
#                 num += 1
#             x += 1
#             y += 1

#         direction = (direction + 1) % 4

#     return answer

# print(solution(4))

# deque GPT
from collections import deque

def solution(n):
    answer = [[0] * n for _ in range(n)]  # n x n 크기의 2차원 배열 생성
    direction = [(1, 0), (0, 1), (-1, -1)]  # 이동 방향 (아래, 오른쪽, 위-왼쪽)
    x, y = 0, 0  # 현재 위치 좌표
    num = 1  # 배열에 채워질 숫자

    queue = deque()
    queue.append((x, y, 0))

    while queue:
        x, y, d = queue.popleft()
        answer[x][y] = num
        num += 1

        dx, dy = direction[d]
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n and answer[nx][ny] == 0:
            queue.append((nx, ny, d))
        else:
            x, y = x + direction[d][0], y + direction[d][1]
            d = (d + 1) % 3
            nx, ny = x + direction[d][0], y + direction[d][1]
            if 0 <= nx < n and 0 <= ny < n and answer[nx][ny] == 0:
                queue.append((nx, ny, d))

    # 결과 반환
    result = []
    for row in answer:
        result.extend(row)
    return result

print(solution(4))