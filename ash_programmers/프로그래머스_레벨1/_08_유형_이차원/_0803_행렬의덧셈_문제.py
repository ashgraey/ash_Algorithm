# https://school.programmers.co.kr/learn/courses/30/lessons/12950
'''
문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

입출력 예
arr1	        arr2	        return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	    [[3],[4]]	    [[4],[6]]
'''
# 통과 안됨 ㅜㅜ
# def solution(arr1, arr2):
#     answer = []
#     for i in range(len(arr1)) :
#         a = arr1[i]
#         b = arr2[i]
#         temp = []
#         temp.append(a[0] + b[0])
#         # 길이의 따른 예외처리
#         if len(a) > 1 and len(b) > 1 :
#             temp.append(a[-1] + b[-1])
        
#         answer.append(temp)
#     return answer


# arr1 = [[1,2],[2,3]]
# arr2 = [[3,4],[5,6]]
# # arr1 = [[1],[2]]
# # arr2 = [[3],[4]]

# a = solution(arr1, arr2)
# print(a)

# 너무 쉬웠자네.. 
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)) :
        answer.append([])
        for j in range(len(arr1[i])) :
            temp = arr1[i][j] + arr2[i][j]
            answer[i].append(temp)
    
    return answer



# arr1 = [[1,2],[2,3]]
# arr2 = [[3,4],[5,6]]
arr1 = [[1],[2]]
arr2 = [[3],[4]]

a = solution(arr1, arr2)
print(a)