
"""
    [1] 아래문자열에서  두글자씩 순서대로 잘라서 리스트에 담아서 출력하시오.
    [2] 공백도 글자에 포함시킨다.
    [3] 단, 두글자전부 알바펫이여야한다. 

        [예시1]
            [1] s = "e=m*c^2  
            [2] [ "e="  , "=m" , "m*" , "*c" , "c^" , "^2" ] 
            [3] 정답 : []
        [예시2]
            [1] s = shake hands
            [2] ["sh" , "ha" , "ak" , "ke" , "e " , " h" , "ha" , "an" , "nd" , "ds"]
            [3] 정답 : ["sh" , "ha" , "ak" , "ke" ,  "ha" , "an" , "nd" , "ds"]

"""

s = "e=m*c^2"
# s = "shake hands"
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

answer = [] 
# result = []
for i in range(len(s) - 1) :
    temp = ""
    temp += s[i]
    temp += s[i + 1]
    # result.append(temp)

    cnt = 0 
    for j in temp :
        if j in abc :
            cnt += 1 
        
    
    if cnt == 0 or cnt == 1 : 
        pass
    else :
        answer.append(temp)
        

print(s)
# print(result)
print(answer)




