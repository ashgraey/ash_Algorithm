'''
문제 보물 //

알고리즘 분류//
그리디 
정렬 

키워드//
a 리스트만 움직일 수 있다. 즉 재배열이 가능하다.

풀이//
일단 a만 재배열이 가능해서 오름차순을 정렬했다. 
b의 max값을 추출해서 max * a[i] 값을 토탈에 +했다. 
max의 값이 내림차순으로 변화시키는 부분은 일단은 copy본을 만들어 copy[maxIdx] = False를 추가하는 방식을 사용해보았다. 
자꾸 런타임에러가 떴는데 문제는 maxIdx의 초기화 식을 안 적어서였다.
답을 보니 b도 재배열이 가능하네 쩝;;

'''
import sys 
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

copy = []
for i in b :
    copy.append(i)

a.sort()
# print(a)
# print(copy)

total = 0
for i in range(len(b)) :
    max = 0 
    maxIdx = 0 # 변수 초기화 하나 안했다고 런타임에러 계속뜸
    for j in range(len(b)) :
        if max < copy[j] :
            max = b[j]
            maxIdx = j
    
    total += (max) * a[i]
    copy[maxIdx] = False
    # print(b)

print(total)
# print(b)