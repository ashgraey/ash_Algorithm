'''
문제 뒤집기//

알고리즘//
문자열
그리디

키워드//
문자열도 배열이라는걸 자꾸 까먹는거 같다.
문제해결법은 여러가지 이다. 
1번 방법 : 0이나 1중 다른 숫자를 만날 때마다 cnt를 올리는 것(이건 잘 이해가 안됨)
2번 방법 : split을 이용하여 0과 1을 분리시키고 0과 1의 묶음을 개수를 구하여 작은값을 뒤집는다는 아이디어

2번 방법을 아이디어는 떠올렸지만 
문자열 split을 하고 난 뒤 2차배열로 바뀐다는것을 인지하지 못하여 자꾸만 맴돌았다.
for if in을 사용하여 반복을 돌리고 0이나 1이 포함된 배열을 만나면 카운트를 해주면 0이나 1의 묶음을 구할 수 있다.
문자열적으로 해결한 케이스
'''
import sys
input = sys.stdin.readline

s = input().rstrip()

zero = s.split("1")
one = s.split("0")

print(zero) 
print(one) 
z_cnt = 0 
for i in zero :
    if "0" in i :
        z_cnt += 1

o_cnt = 0 
for i in one :
    if "1" in i :
        o_cnt += 1 

answer = [z_cnt, o_cnt]
print(min(answer))