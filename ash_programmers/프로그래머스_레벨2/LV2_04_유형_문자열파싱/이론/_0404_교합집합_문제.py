
"""
    다음 a와 b의 교집합 갯수와 합집합 개수를 구하시오.

    교집합 은 1,4,3  이렇게 3개이고 
    합집합 은 1,1,2,3,4,5,6,7 이렇게 8개이다. 

"""
a = [1,4,3,7]
b = [1,1,2,3,4,5,6]


for i in range(len(a)) :
    b.append(a[i])

c = set(b)
print(c) # 합집합 : 두 집합 간의 중복을 제거한 집합
print(b)
for i in range(len(c)) :
    if c[i] in b :
        idx = b.index(c[i])
        del(b[idx])
print(b) 

