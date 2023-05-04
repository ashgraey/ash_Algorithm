"""
[문제]
    아래 a 이차원배열에서 "o" 은 값이 있다는 뜻이고 "x" 는 없다는뜻이다.
    "o" 은 중력을 가지고있어서 아래로 내려간다. 
    전부 내려간이후의 모습을 출력하시오.

    [예시]
        ["o","o","o","o"],
        ["o","x","o","o"],
        ["x","x","o","x"],
        ["x","o","x","o"],

        아래와 같이된다. 
        ["x","x","x","x"],
        ["x","x","o","o"],
        ["o","o","o","o"],
        ["o","o","o","o"],

"""

a = [
    ["o","o","o","o"],
    ["o","x","o","o"],
    ["x","x","o","x"],
    ["x","o","x","o"],
]

for i in range(len(a)) : # x축
    for j in range(len(a)) :
        if a[j][i] == "o" :

            temp = ""
            for k in range(j+1, len(a)) :
                if a[k][i] == "x" :
                    temp = "x"
                    a[k][i] = a[j][i] 
                    a[j][i] = temp
    
for i in a :    
    print(i)
