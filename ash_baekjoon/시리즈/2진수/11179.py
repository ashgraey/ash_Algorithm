'''
문제 2진수 뒤집기//
'''
# 10진수 => 2진수 => 2진수 뒤집기 => 10진수

import sys
input = sys.stdin.readline

def get_bianry(a) :

    # 10진수보다 큰 2의 배수를 받는다. 
    b = 1 
    while a >= b : 
        b *= 2 
    
    # a = 13, b = 16
    st = ''
    while True :
        if b == 0 :
            break
        
        s = a // b
        st += str(s)

        a %= b 
        b //= 2
    
    return st[1:]

n = int(input())

binary = get_bianry(n)
r_binary = ''.join(reversed(binary))
print(int(r_binary, 2))