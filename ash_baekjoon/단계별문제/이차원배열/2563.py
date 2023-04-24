'''
문제 색종이//

-canvas-
w * h : 100 * 100

-unit-
w * h : 10 * 10
'''
# 멍충이 다 풀어놓고는ㅜㅜ
# 하..

canvas = []
for i in range(100) :
    temp = []
    for j in range(100) :
        temp.append(0)
    canvas.append(temp)


import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    w, h = map(int, input().split())

    for row in range(w, w + 10) :
        for col in range(h, h + 10) :
            canvas[row][col] = 1 

# for i in canvas :
#     print(canvas)

result = 0
for i in canvas :
    result += i.count(1)

print(result)