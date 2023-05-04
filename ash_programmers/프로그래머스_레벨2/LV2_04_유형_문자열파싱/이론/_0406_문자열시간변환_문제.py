import math
arr = ["12:04,13:00" , "21:47,23:45"]

brr = []
"""
위 arr 배열은 시간을 표현한것이다. 
12:04분이 시작이고 13:00 이 마감이라고 했을때, 
각각의 시간차를 brr배열에 저장하시오. 

brr = [60, 120]
"""
time = []
for i, v in enumerate(arr) :
    temp = []
    coin = v.split(",")
    coin[0] = coin[0].split(":")
    coin[1] = coin[1].split(":")
    time.append(coin[0])
    time.append(coin[1])

# print(time)
for i in time :
    print(i)

result = []
temp2 = []
cnt = 0
for i in range(len(time)) :
    if i % 2 == 0 :
        # result.append(temp2)
        temp2 = []
    
    temp2.append(((int(time[i][0]) * 60)) + int(time[0][1])) # 분단위를 더하면 된다. 
    # result.append(temp2)
    cnt += 1
    if cnt == 2 :
        result.append(temp2)
        cnt = 0 
    # print(i)
print(result)

total = []
for i in range(len(result)) :
    tot  = result[i][0] - result[i][-1]

    if tot < 0 :
        tot = -tot
    
    total.append(tot)

print(total)