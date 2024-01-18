
# 이차원 배열 1 ~ 40
# init
zero_pan = []
for i in range(4) :
    temp = []
    for j in range(10) :
        temp.append(0)
    zero_pan.append(temp)

# for _ in zero_pan :
#     print(_)

# 게임판 구현
num = 1
for i in range(10) :
    for j in range(4) :
        zero_pan[j][i] += num
        num += 1
    
A, B = map(int, input().split())

A_idx = []
B_idx = []
for i in range(len(zero_pan)) :
    for j in range(len(zero_pan[i])) :
        if zero_pan[i][j] == A :
            A_idx.append(i)
            A_idx.append(j)
        elif zero_pan[i][j] == B :
            B_idx.append(i)
            B_idx.append(j)

# print(A_idx, B_idx)
x = A_idx[0] - B_idx[0]
if x < 0 :
    x = -x
y = A_idx[1] - B_idx[1]
if y < 0 :
    y = -y

distance = x + y
print(distance)