'''
문제 더하기 사이클//

알고리즘//
구현, 수학

아이디어//
1. 10보다 작은수는 앞에 0을 붙인다. 
2. n의 2번째 수와 더한 값을 2번째수를 조합하여 다음 사이클을 만든다.
3. cnt값을 올리고 초기값과 같은 값이 나오면 멈춘다.

키워드// 

'''
import sys
input = sys.stdin.readline

# n = int(input())
# result = str(n)
# cnt = 0
# while True :
    
#     n = str(n)
#     sec_n = int(n[0]) + int(n[1])

#     if len(n) > 1 :
#         n = n[1]
#     else : 
#         n = "0" + n
#         n = n[1]

#     sec_n = str(sec_n)
#     if len(sec_n) > 1 : 
#         sec_n = sec_n[1]
#     else : 
#         sec_n = sec_n
    
#     if result == n :
#         print(cnt)
#         break
    
#     n += sec_n
#     cnt += 1 
    
#     print(n + sec_n)


n = int(input())    
bk = n
cnt = 1 
while True :

    n1 = n // 10
    n2 = n % 10 
    n3 = n1 + n2

    if n3 >= 10 :
        n3 = str(n3)
        n = str(n2) + n3[1]
        n = int(n)
    else :
        n = str(n2) + str(n3)
        n = int(n)

    if n == bk :
        print(cnt)
        break

    cnt += 1