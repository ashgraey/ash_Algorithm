N = int(input())
abc = "abcdefghijklnmopqrstuvwxyz"
fir_name_list = []
for _ in range(N) :
    fir_name = input()
    fir_name_list.append(fir_name[0])

# print(fir_name_list)
result_list = []
for i in abc :
    cnt = 0
    for j in fir_name_list :
        if i == j :
            cnt += 1 
    if cnt >= 5 :
        result_list.append(i)
        
# print(result_list)
if len(result_list) == 0 :
    print("PREDAJA")
else :
    result_list.sort()
    result = ''.join(result_list)
    print(result)