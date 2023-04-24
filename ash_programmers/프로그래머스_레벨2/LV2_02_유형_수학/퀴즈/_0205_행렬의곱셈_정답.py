# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    # 먼저 합쳐진 행렬을 새로운 list로 0을 채워 초기화한다.
    # 4 * 3
    array = [[0 for col in range(len(arr2[0]))] 
    for row in range(len(arr1))]
    # print(array)

    for i in range(len(arr1)): # 4
        for j in range(len(arr2[0])): # 3
            total = 0
            for k in range(len(arr1[0])): # 2
                total += arr1[i][k] * arr2[k][j] # arr1[i][k] == arr1[3][1] * arr2[k][j] == arr2[1][2]
            array[i][j] = total # array[i][j] == array[3][2]


    return array

arr1 = [[1, 2], 
        [3, 4], 
        [5, 6],
        [7, 8]]

arr2 = [[10, 11, 12], 
        [13, 14, 15]]

r = solution(arr1 , arr2)
print(r)

"""
행렬
말그대로 2차원 배열에서 행(가로) * 열(세로)을 곱한 새로운 배열을 만드는 작업
"""