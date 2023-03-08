# https://school.programmers.co.kr/learn/courses/30/lessons/92334

# 입출력 예시만 통과함 다른 테스트 케이스를 많이 통과 못함 ㅜㅜ
# def solution(id_list, report, k):
#     answer = []
#     reportList = []
#     for i in range(len(report)) :
#         temp = report[i].split(" ")
#         reportList.append(temp)
#     # print(reportList)
    
#     # count
#     cntList = []
#     resultList = []
#     for i in range(len(id_list)) :
#         cnt = 0 
#         temp = []
#         # temp.append(id_list[i])
#         for j in range(len(reportList)) :
#             if id_list[i] == reportList[j][-1] :
#                 cnt += 1
#             if id_list[i] == reportList[j][0] :
#                 temp.append(reportList[j][-1])
#         cntList.append(cnt)
#         resultList.append(temp)
#     # print(cntList)
#     # print(resultList)

#     tempList = []
#     for i in range(len(cntList)) :
#         if cntList[i] == k :
#             tempList.append(id_list[i])
#     # print(tempList) 

#     for i in range(len(resultList)) : 
#         cnt = 0
#         for j in range(len(resultList[i])) :
#             for k in range(len(tempList)) :
#                 if resultList[i][j] == tempList[k] :
#                     cnt += 1 
#         answer.append(cnt)

    
#     return answer

# id_list = ["muzi", "frodo", "apeach", "neo"]
# id_list = ["con", "ryan"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# report = ["ryan con","ryan con","ryan con","ryan con","ryan con"]
# k = 3
# result = solution(id_list , report , k)
# print(result)

# 강사님 정답
# 대충 이해함, 딕셔너리(제이슨)을 잘 이해해야한다.
def solution(id_list, report, k):
    answer = []
    all = {}
    for i in range(len(report)):
        a = report[i]
        token = a.split(" ")
        # print(token)
        user = None
        # print(token[1])
        # print(all)
        if token[1] in all:
            user = all[token[1]]
            user[token[0]] = 1
        else:
            user = {token[0] : 1}
        all[token[1]] = user   
        # print(all)  
    print(all) # {'frodo': {'muzi': 1, 'apeach': 1}, 'neo': {'frodo': 1, 'muzi': 1}, 'muzi': {'apeach': 1}}
    
    keys = all.keys()
    print(keys) # dict_keys(['frodo', 'neo', 'muzi'])
    answer = [0 for i in range(len(id_list))] # [0, 0, 0, 0]
    print(answer)
    for key in keys:
        if len(all[key]) >= k:
            # print(key)
            # print(len(all[key])) 2 2
            d = all[key]
            # print(d)
            for i in range(len(id_list)):                
                if id_list[i] in d.keys():
                    answer[i] += 1      
    return answer
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
result = solution(id_list , report , k)
print(result)
