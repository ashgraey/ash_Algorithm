'''
문제 강의실 배정//

알고리즘//
그리디
우선순위 큐
정렬
자료구조

키워드//
1. 현재 회의시간의 마치는 시간보다 빠르게 개설되는 회의 시간이 있으면 강의실을 개설해야함 push
2. 현재 회의시간의 마치는 시간과 겹치거나 느리게 개설되는 회의 시간에는 강의실 개설을 하지 않아도 된다.

# 우선순위 큐인 heap자료구조에 대한 이해가 아직 많이 낮은거 같다 
대충 이해는 되었지만 음 확실히 스스로 구현하라면 아직은 못할거 같다.
핵심은 마치는 시간과 시작시간이 연결되면 pop으로 기존의 마치는 시간을 버린고 새로운 마치는 시간을 추가하면서 계속 연결시키는 것

'''
import sys, heapq
input = sys.stdin.readline
n = int(input())

time = []
for i in range(n) :
    start, end = map(int, input().split())
    time.append([start, end])

# 시작 시간으로 정렬
time.sort()
# print(time)

# 마치는 시간 초기값
heap = []
heapq.heappush(heap, time[0][1])
# print(heap)

# 쉽게 설명해서 이어지는 회의시간은 회의실을 새로 만들지 않고 계속 최신화를 시켜줌
# 마치는 시간보다 개설되는 시간이 빠른 회의는 회의실을 개설시켜줌
# heap을 사용해서 가장 빨리 마치는 시간으로 정렬되어 비교

# 마치는 시간과 시작하는 시간을 비교
for i in range(1, n) :
    if time[i][0] < heap[0] : # 다음 회의 시작시간 < 현재 회의 마치는 시간
        heapq.heappush(heap, time[i][1]) # 새로운 회의실 개설
    else : 
        heapq.heappop(heap) # 기존 회의실 시간을 빼고
        heapq.heappush(heap, time[i][1]) # 새로운 회의시작 시간의 마치는 시간을 넣음

# 최신화된 회의실갯수가 나옴
print(len(heap))