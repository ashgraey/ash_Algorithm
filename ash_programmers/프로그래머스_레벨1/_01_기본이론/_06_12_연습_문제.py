"""
    [문제]
        b의 값의 -1 이나 + 1한 값이 a에 있으면 a의 값에서 b의 값을 전부 삭제후 출력하시오.
    [예시]
        b의 3 은 삭제할수없음
        b의 4 + 1 은 5 이므로 5삭제 a = [1,7,8]
        b의 6 + 1 은 7 이므로 7삭제 a = [1,8]
    [정답]
        [1,8]
"""

a = [1,5,7,8]
b = [3,4,6]

# 3/31 한번 더 풀어보자
for num in b :
    num_min = num - 1 
    num_pls = num + 1
    if num_min in a :
        idx1 = a.index(num_min)
        del(a[idx1])
    if num_pls in a :
        idx2 = a.index(num_pls)
        del(a[idx2])

print(a)

# for i in range(len(b)) :
#     c = b[i] + 1 
#     d = b[i] - 1 

#     if c in a :
#         idx = a.index(c)
#         del(a[idx])
#     if d in a :
#         idx = a.index(d)
#         del(a[idx])

# print(a)



