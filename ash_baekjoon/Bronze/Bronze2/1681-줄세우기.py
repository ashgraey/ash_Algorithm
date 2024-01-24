N, L = input().split()

N = int(N)
num = "1"
cnt = 0 
while True : 
    num_cnt = num.count(L)
    # print(num_cnt)
    if num_cnt == 0 :
        # num = int(num)
        cnt += 1 
        # num += 1
    if cnt == N :
        break

    num = int(num)
    num += 1
    num = str(num)


print(num)

# num = "1"
# print(num.count(L))