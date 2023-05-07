'''
문제 그대로 출력하기2//

알고리즘//
문자열
구현

키포인트//
프로그램에서 발생하는 예외사항
try : 
    명령문 
except :
    오류/예외를 처리해줄 핸들러
'''
# import sys
# input = sys.stdin.readline

while True :
    try :
        print(input())
    except EOFError :
        break 
