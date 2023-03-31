"""
    [딕셔너리 정렬]
"""
# items() 내장함수 : dict의 key와 value를 동시에 얻을 수 있다
# keys() : key만
# valuse() : value만
d = {"dream": 0, "car": 99, "blockdmask": 1, "error": 30, "app": 20}

print(d.items())
ditem = d.items()
# print(ditem[0])
# print(d.values())
"""
[1] 딕셔너리 key기준 정렬 (오름차순) 
"""
# items() 내장함수를 정렬기준으로 만들어도 key값이 정렬 기준이 되는듯
sortedItem = sorted(d.items())
print(sortedItem)

"""
[2] 딕셔너리 key기준 정렬 (내림차순)
"""
sortedItem = sorted(d.items(), reverse=True)
print(sortedItem)

"""
[3] 딕셔너리 value기준 정렬 (오름차순) 
"""
sortedItem = sorted(d.items(), key=lambda x: x[1])
print(sortedItem)

"""
[4] 딕셔너리 value기준 정렬 (내림차순) 
"""
sortedItem = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(sortedItem)
