'''
문제 다음소수//
'''
# 시간초과
# import sys, math
# input = sys.stdin.readline

# tc = int(input())

# for _ in range(tc) : 
#     num = int(input())
    
#     # print(arr_num)
#     while True :

#         cnt = 0 
#         for i in range(2, int(math.sqrt(num)) + 1) : 
#             if num % i == 0 : 
#                 cnt += 1
#                 break  

#         if cnt == 0 :
#             print(num)
#             break
#         else :
#             num += 1

# 에스테라토네스의 체
import sys, math
input = sys.stdin.readline

def get_prime(n) :
    arr_n = list(range(2, n + 1))
    # print(arr_n)
    
    print(arr_n)
    return True



tc = int(input())

for _ in range(tc) :
    num = int(input())

    while True :
        prime_n = get_prime(num)
        
        if prime_n : 
            break 
        else :
            num += 1
    
        # break