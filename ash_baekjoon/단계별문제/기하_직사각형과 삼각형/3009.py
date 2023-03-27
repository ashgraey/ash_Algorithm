'''
문제 네 번째 점// 
세 점이 주어졌을 때, 
축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다.
좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
'''

x_idx = []
y_idx = []

for _ in range(3) :
    x, y = map(int, input().split())

    x_idx.append(x)
    y_idx.append(y)

# print(x_idx)
# print(y_idx)

for i in range(3) :
    if x_idx.count(x_idx[i]) == 1 :
        x4 = x_idx[i]
    if y_idx.count(y_idx[i]) == 1 :
        y4 = y_idx[i]
    
print(x4, y4)
