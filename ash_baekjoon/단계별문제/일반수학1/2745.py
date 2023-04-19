'''
문재 진법 변환//

어떠한 수를 0을 제곱하면 항상 1이 나온다.

hint//
2진수 10진수로 변환과정
1     0     1     0
1*2^3 + 0*2^2 + 1*2^1 + 0*2^0
8 + 2 
10
'''

n, b = input().split()
num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = ''.join(reversed(n)) # 문자열 뒤집기, 진수변환은 역순으로 일어나기 때문
b = int(b)

# print(num.index("Z"))
# print(n)
result = 0 
for i in range(len(n)) :
    result += num.index(n[i]) * b ** i

print(result)
    


# print(abc_num)
# print(n, b)