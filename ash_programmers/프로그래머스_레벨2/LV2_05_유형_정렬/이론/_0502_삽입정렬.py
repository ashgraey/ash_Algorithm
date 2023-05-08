# https://jinyes-tistory.tistory.com/30

'''
<삽입정렬>
삽입 정렬은 정렬이 필요한 데이터를 찾고 적절한 위치에 삽입하며 정렬하는 알고리즘입니다. 
삽입 정렬은 필요할 때만 데이터를 비교하고 삽입하기 때문에 데이터가 어느 정도 정렬되어 있을 때 더욱 효율적으로 동작합니다. 
이러한 특징 덕분에 정렬 상태와 상관없이 모든 데이터를 일일이 비교하며 정렬하는 방식인 선택 정렬보다 일반적으로 효율적입니다.
'''

def insert_sort(arr):
    for i in range(len(arr)):
        last = i
        for j in range(i):
            if arr[last] > arr[last-1]:
                # temp = arr[last]
                # arr[last] = arr[last-1]
                # arr[last-1] = temp
                arr[last], arr[last - 1] = arr[last - 1], arr[last]
            else:
                break
            last -= 1
        print(arr)
    print(arr)

    pass


a = [34,65,3,5,8,9,12,2,5,100]
insert_sort(a)