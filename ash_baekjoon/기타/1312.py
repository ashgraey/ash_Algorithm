'''
문제 소수//
레알 수학 문제였네 ㅋㅋㅋㅋ
for case1.

25 % 7 = 4 * 10 = 40

40 // 7 = 5(result)

 

for case2.

40 % 7 = 5 * 10 = 50

50 // 7 = 7(result)

 

for case3.

50 % 7 = 1 * 10 = 10

10 // 7 = 1(result)

 

for case4.

10 % 7 = 3 * 10 = 30

30 // 7 = 4(result)

 

for case5.

30 % 7 = 2 * 10 = 20

20 // 7 = 2(result)

-> end 정답 : 2
'''
import sys
input = sys.stdin.readline

a, b, n = map(int, input().split())

for i in range(n) :
    a = (a % b) * 10
    result = a // b
print(result)