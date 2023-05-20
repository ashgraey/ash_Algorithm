'''
문제 배열 합치기//

알고리즘//
정렬

키포인트//
1) sort() 시간초과 날까? => 시간초과 안남
2) 파이썬은 + 연산자로 배열이 합쳐진다. 
3) 출력시 반복문을 돌렸지만 비효율적 join() 메서드를 통해 문자열로 만들고 출력하는것이 효율이 좋을거 같다.
4) 입력을 정수로 받으라는 조건이 있었다. 입력은 정수로 받고 sort()를 할때 map을 이용하여 String으로 형변환 시켜주면 문제가 되지 않는다.
=> map을 조금더 공부해야할거 같다.
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# nList = list(map(int, input().split()))
# mList = list(map(int, input().split()))

# totList = sorted(nList + mList)

# # print(totList)
# # 기존의 반복문을 돌려 요소 하나하나를 출력
# for v in totList :
#     print(v, end = " ")

# join()을 활용하여 배열을 문자열로 만드려면 배열의 요소들이 String 타입이여야한다.
nList = list(map(int, input().split()))
mList = list(map(int, input().split()))
totList = map(str, sorted(nList + mList)) # key포인트 map을 활용하여 합친두배열의 정렬된 값을 str으로 형변환시킨다.
totWords = " ".join(totList)

print(totWords)