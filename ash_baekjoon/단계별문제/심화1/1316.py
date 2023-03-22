'''
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
'''

# 아이디어 : 딕셔너리의 활용 
# 설명 : set을 이용하여 단어의 중복을 없앤 뒤 원소들을 딕셔너리에 저장
# 저장한 딕셔너리의 키와 일치하는 word의 원소들의 인덱스를 배열로 받아 각 키에 저장
# 각 키의 길이가 1이면 그룹단어이므로 예외처리, 각 키의 길이가 1이 아닌 경우
# 배열의 담긴 인덱스 번호의 연속성을 검사, 연속되지 않은 배열 발견시 break

# n = int(input())

# answer = 0 
# for i in range(n) :
#     word = input()
    
#     check = True

#     set_word = set(word)
#     # print(set_word)

#     # 딕셔너리에 배열을 넣을 수 있음
#     dict = {}
#     for i in set_word :
#         dict[i] = []
#     # print(dict)

    
#     # 여기서 i는 key값
#     for i in dict :
#         temp = []
#         for j in range(len(word)) :
#             if i == word[j] :
#                 # idx = word.index(word[j])
#                 temp.append(j)
#         dict[i] = temp
#     # print(dict)
                    
#     cnt = 0
#     for k, v in dict.items() :
#         # print(k, v)
#         # 중복이 없는 문자열 예외처리
#         if len(v) == 1 :
#             cnt += 1 
#         else :
#             tempV = v[0]
#             # print(v[0])
#             for j in range(1, len(v)) :
#                 if tempV - v[j] == -1 or tempV - v[j] == 1 :
#                     tempV = v[j]
#                 else :
#                     check = False 
#                     break

#     # print(check)
#     if cnt == len(dict) or check == True :
#         answer += 1
# print(answer) 


# 다른 사람 풀이 1)
# N = int(input())
# for i in range(N):
#     a = input()
#     print(list(a))
#     print(sorted(a, key=a.find))
#     if list(a) != sorted(a, key=a.find):
#         N -= 1
# print(N)

# 다른 사람 풀이 2)
# 그룹단어란 연속되는 중복만을 허용, 만약 연속된 중복이 아니고 뒤의 원소 중에 중복이 있다면 그것은 그룹단어가 아니다.
N=int(input())
cnt=0
for i in range(N):
    word = input()  

    bl_=True
    for j in range(len(word)-1):
        # 연속되는 원소의 중복인지 검사
        if word[j]!=word[j+1]:
            # print(word[j+1:])

            # appy 안에 word[j] 즉, h가 있는지 확인
            if word[j] in word[j+1:]: # 슬라이싱 [시작인덱스:] => 시작인덱스에서 끝 인덱스까지 잘라줌 
                bl_=False
                break
    if bl_:
        cnt+=1
print(cnt)



    