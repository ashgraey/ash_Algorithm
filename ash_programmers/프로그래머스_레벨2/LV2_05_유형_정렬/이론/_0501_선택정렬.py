# https://heytech.tistory.com/57

'''
<선택정렬>
기존의 내가 자주해오던 방식의 정렬
인덱스 0부터 시작 => 가장 작은값고 인덱스0의 값을 교체 => 인덱스1로 증가 => 다시 가장 작은값과 인덱스1 교체
시간복잡도는 O(n^2)으로 효율성이 좋지는 않다.
'''

# 나의 구현
def select_sort(a) :
    for i in range(len(a)) :
        min_idx = i
        for j in range(i + 1, len(a)) :
            if a[min_idx] > a[j] :
                min_idx = j
        
        a[i], a[min_idx] = a[min_idx], a[i]

    return a

arr = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print("정렬 전 : ", arr)
print("정렬 후 : ", select_sort(arr))

# 선생님 코드
# def selection_sort(a):
#     for i in range(len(a)):
#         minIndex = i
#         minValue = a[i]
#         for j in range(i + 1, len(a)):
#             if minValue > a[j]:
#                 minIndex = j
#                 minValue = a[j]
            
#         a[i], a[minIndex] = a[minIndex], a[i]

# a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
# print('정렬 전:\t', end='')
# print(a)
# selection_sort(a)
# print('정렬 후:\t', end='')
# print(a)