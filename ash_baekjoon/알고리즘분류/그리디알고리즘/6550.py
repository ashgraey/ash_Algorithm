'''
문제 부분 문자열//

알고리즘//
문자열
그리디 

아이디어//
1. s문자열의 요소가 t문자열에 있는지 count한다.
2. t문자열의 요소를 인덱스로 받아 indexArr에 저장한다.
3. if s문자열의 길이와 count의 값이 같은지 확인다. 
    3 - 1) if indexArr가 오름차순이면 Yes
    3 - 2) else면 No
4. else No
'''
import sys
input = sys.stdin.readline

# 왜 틀렸습니다??
# while True :
#     try :
#         s, t = input().rstrip().split()
# # print(s, t)

#         idx = 0
#         # indexArray = []
#         cnt = 0 
#         for i in range(len(s)) :
#             for j in range(idx, len(t)) :
#                 if s[i] == t[j] :
#                     idx = j
#                     cnt += 1
#                     # indexArray.append(idx)
#                     break
#         # print(indexArray)
#         # print(cnt)
#         if len(s) == cnt :
#             print("Yes")
#         else : 
#             print("No")
        
#     except :
#         break

while True :
    try : 
        s, t = input().rstrip().split()

        # cnt = 0
        idx = 0
        ck = False
        for i in range(len(t)) :
            if t[i] == s[idx] :
                # cnt += 1
                idx += 1
                if idx == len(s) :
                    ck = True
                    break
        
        if ck : 
            print("Yes")
        else :
            print("No")
    
    except :
        break


'''
인터넷 답안//
import sys
input = sys.stdin.readline

while True:
    ss = input().rstrip()
    - 굳이 try expect를 쓰지 않다도 된다.
    - if not ss => ss의 값이 없는 경우 False => not False == True
    - ss에 값이 안들어오면 break문 실행
    if not ss:
        break
    
    - split으로 s, t 배열로 분류
    s, t = ss.split()
    flag = 0
    idx = 0
    

    for i in range(len(t)):
        - t를 기준으로 
        if t[i] == s[idx]:
            idx+=1
            if idx == len(s):
                flag = 1
                break
    
    if flag == 1:
        print('Yes')
    else:
        print('No')
'''

