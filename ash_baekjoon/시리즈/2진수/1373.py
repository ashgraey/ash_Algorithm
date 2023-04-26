'''
문제 2진수 8진수//
'''
# 변환과정을 두번 걸쳐서 써보자
# 1. 10진수로 변환 2.8진수로 변환
import sys
input = sys.stdin.readline

binary = input().rstrip()

oct_bi = oct(binary)
print(oct_bi)

# 2진수를 10진수로
# print(len(binary))
demical = 0 
for i in range(len(binary)) :
    # print(binary[i])
    demical += int(binary[i]) * (2 **( len(binary) - i - 1))
# print(demical)
# print(demical)
# print(int(binary, 10))

# 10진수를 8진수로
# octal = ''
# while demical > 0 :
#     remain = demical % 8
#     octal = str(remain) + octal
#     demical //= 8

# print(octal)
octal = oct(demical)
octal = octal[2:]
print(int(octal))