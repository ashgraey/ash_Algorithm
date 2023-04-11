'''
문제 듣보잡//
'''
# 둘다 딕셔너리로 해야함
# 배열 쓰는 순간 시간초과 계속 남
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

not_heard = {}
for _ in range(n) :
    not_heard[input().strip()] = True
# print(dict) 

not_seen = {}
for _ in range(m) :
    find = input().strip()
    if find in not_heard :
        not_seen[find] = True

# print(not_seen)

print(len(not_seen))
for i in sorted(not_seen.keys()) :
    print(i)
    
# name1 = []
# name2 = []
# for _ in range(n) :
#     name1.append(input().strip())

# for _ in range(m) :
#     name2.append(input().strip())


# size1 = len(name1)
# size2 = len(name2)

# result = []
# if size1 >= size2 :
#     for i in name1 :
#         if i in name2 :
#             result.append(i)

# elif size1 <= size2 :
#     for i in name2 :
#         if i in name1 :
#             result.append(i)
# # print(name1, name2) 
# # print(result)
# print(len(result))
# for i in result :
#     print(i)