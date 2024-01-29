my = list(map(int, input().split()))
answer = list(map(int, input().split()))

result_list = []
result = 0
for i in range(len(my)) :
    if my[i] == answer[i] :
        result_list.append(str(i + 1) + " : O" + " Answer : " + str(answer[i]))
        result += 5
    else :
        result_list.append(str(i + 1) + " : X" + " Answer : " + str(answer[i]))

# print(result_list)
for i in result_list :
    print(i)

print(result)
