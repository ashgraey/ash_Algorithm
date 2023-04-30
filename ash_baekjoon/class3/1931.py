'''
문제 회의실 배정//

알고리즘 분류//
그리디 
정렬

분석//
그리디 알고리즘과 정렬을 사용해야하는 문제로
아이디어는 생각보다 간단하다. 끝나는 시간 정렬을 사용해서 가장 일찍 끝나는 시간을 변수 end_time에 담는다. 
리스트를 돌면서 시작 시간이 끝나는 시간과 같거나 크면 변수 end_time에 큰 시작 시간을 담고 count += 1 를 한다.
생각해보면 거스름돈이랑 거의 동일한 그리디 알고리즘인듯 문제는 정렬인데
1차 시도 : lambda로 끝나는 시간을 오름차순 정렬으로 풀려고 했다. lambda x : arr[0][1] 인자값을 바로 전달하려니 틀렸던거 같다.
n차 시도 : 올바른 방법으로 lambda를 사용하니 풀렸다. lambda x : (x[1], x[0]) => gpt해설로는 두번째값을 오름차순 정렬한다. 같은 값이 나오면 첫버째값을 오름차순으로 정렬한다.
'''
import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n) :
    start, end = map(int, input().split())
    arr.append([start, end])

# lambda 정렬 인자 차이로 계속 틀렸습니다 떴음.
arr = sorted(arr, key = lambda x : (x[1], x[0]))
# arr = sorted(arr, key = lambda x : arr[0][1])

# for i in range(len(arr)) :
#     print(arr[i])

end_time = arr[0][1]
cnt = 1
for i in range(1, len(arr)) :
    if end_time <= arr[i][0] :
        end_time = arr[i][1]
        cnt += 1
        # print(arr[i]) 
print(cnt)



