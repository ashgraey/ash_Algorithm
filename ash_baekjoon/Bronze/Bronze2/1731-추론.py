
N = int(input())

num_list = []
if 3 <= N <= 50 :
    for _ in range(N) :
        num_list.append(int(input()))

num_diff = num_list[1] - num_list[0]
num_diff2 = num_list[1] // num_list[0]

# 등차수열인지
if (num_list[1] + num_diff) == num_list[2] :
    print(num_list[len(num_list) - 1] + num_diff) 
else :
    print(num_list[len(num_list) - 1] * num_diff2)
