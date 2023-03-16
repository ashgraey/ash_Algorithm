'''
문제
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 
단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값

중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값

최빈값 : N개의 수들 중 가장 많이 나타나는 값

범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력
첫째 줄에는 산술평균을 출력한다. 
소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 
여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.
'''
import sys
input = sys.stdin.readline

# 홀수값만 받기
# while True :
#     n = int(input())
#     if n % 2 == 1 : 
#         break
n = int(input())

nList = [int(input()) for _ in range(n)]
# print(nList)

# 1 산술평균
print(round(sum(nList) / n))

# 2 중앙값
nList.sort()
mid = len(nList) // 2 
print(nList[mid])

# 3 최빈값
# 딕셔너리로 풀어보자
cnt = {}
for i in nList :
    if i in cnt :
        cnt[i] += 1 
    else :
        cnt[i] = 1
print(cnt)

max = cnt.get(max(cnt))
# max = max(cnt.values())
maxCnt = []

# print("max : ", type(max))
for i in cnt :
    if max == cnt[i] :
        maxCnt.append(i) # 최빈값의 key를 저장

if len(maxCnt) > 1 :
    print(maxCnt[1])
else :
    print(maxCnt[0])

# print(max)
# print(maxCnt)
 

# maxCnt = cnt.count(max)
# print(maxCnt)
# print(max(count))


# 최댓값과 최솟값의 차이
min = nList[0]
max = nList[-1]
diff = max - min
print(diff)
# if diff < 0 : 
#     print(-diff)
# else :
#     print(diff)
