"""
[1] 딕셔너리 키묶음찾기
    딕셔너리는 keys() 함수를 이용해서 key값들을 모두 찾은후, key로 value를 찾을수있다. 
"""
# key를 list로 받아서 index를 사용할 수 있을거 처럼보이지만 아님
# key로 value를 찾아야함

di = {"a": 0, "b": 1, "c": 2}
dikey = di.keys()
print(di.keys())
# print(dikey[0])
print("------------------------")

"""
[1] 딕셔너리 출력
    for 문을 활용해서 아래와 같이 출력할수있다.
"""
for key in di.keys():
    print(key, " ", di[key])

print()
for key in dikey :
    print(key, " ", di[key])


for k in di.keys():
    print(k, " ", di[k])
