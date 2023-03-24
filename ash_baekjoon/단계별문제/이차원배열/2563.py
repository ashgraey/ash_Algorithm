'''
문제 색종이//

-canvas-
w * h : 100 * 100

-unit-
w * h : 10 * 10
'''

canvas = []
for i in range(100) :
    for j in range(100) :
        canvas.append(0)

# for i in canvas :
#     print(i)

for i,v in enumerate(canvas) :
    if i % 100 == 0 : 
        print()
    print(v, end = " ")
        