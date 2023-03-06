# https://school.programmers.co.kr/learn/courses/30/lessons/42576

'''
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다.
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

입출력 예
participant	                                        completion	                                return
["leo", "kiki", "eden"]	                            ["eden", "kiki"]	                        "leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	            ["stanko", "ana", "mislav"]	                "mislav"
'''
# 시간초과 뜸, 시간복잡도..
# def solution(participant, completion):
#     for i in range(len(participant)) :
#         ck = False 
#         for j in range(len(completion)) :
#             if participant[i] == completion[j] :
#                 ck = True 
#                 completion[j] = -1
#                 break 
        
#         if ck == False :
#             return participant[i]
    
#     # return 0
        
# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]
# # participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# # completion = ["josipa", "filipa", "marina", "nikola"]

# result = solution(participant , completion)
# print(result)

def solution(participant, completion):
    participant.sort()
    completion.sort()
    # print(participant)
    # print(completion)

    # 정렬 후 명단 확인
    # 다른 값이 없으면 참가자 명단 마지막 값을 return
    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            return participant[i]
    return participant[-1] 
        
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]

result = solution(participant , completion)
print(result)