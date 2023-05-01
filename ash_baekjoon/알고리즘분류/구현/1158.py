'''
문제 요세푸스//

알고리즘//
구현
자료구조
큐

키워드//
요세푸스 순열문제는 큐 구조만 이해하고 있다면 쉽게 풀이가 가능하다. 
1. k의 값이 되기전에 값들은 회전하는 구조니깐 뒤로 보낸다.
2. k 값과 count가 일치하면 answer 배열로 arr의 값을 옮긴다.
n값만큼 반복하면서 조건식을 걸어 빠져나오면 arr이 0 보다 클 때까지 반복문이 돈다.

# 런타임 에러나는 코드
    # for i in range(k) :
    #     if i == k - 1 : 
    #         answer.append(arr.popleft())
    #     else :
    #         arr.append(arr.popleft())
    
    # # print(answer)
    # if len(arr) == 1 :
    #     answer.append(arr.popleft())
    #     break
    
'''
import sys
from collections import deque
# input = sys.stdin.readline

n, k = map(int, sys.stdin.readline().split())
arr = deque(i for i in range(1, n + 1))
# print(arr)

answer = []
while len(arr) > 0 :

    # 런타임 에러나는 코드
    # for i in range(k) :
    #     if i == k - 1 : 
    #         answer.append(arr.popleft())
    #     else :
    #         arr.append(arr.popleft())
    
    # # print(answer)
    # if len(arr) == 1 :
    #     answer.append(arr.popleft())
    #     break

    cnt = 0 
    for i in range(n) :
        cnt += 1
        if cnt == k :
            answer.append(arr.popleft())
            break
        else :
            arr.append(arr.popleft())


# print(answer)
print("<", end = "")
for k, v in enumerate(answer) :
    if k == len(answer) - 1 :
        print(v, end=">")
    else :
        print(v, end =", ")

# print(end = "<")
# for i in range(len(answer)) :
#     if i == len(answer) - 1 :
#         print(answer[i], end = ">")
#     else :
#         print(answer[i], end = ", ")



