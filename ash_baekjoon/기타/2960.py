'''
문제 에라토스테네스의 체//
'''

'''
2 3 4 5 6 7 => 6
소수의 배수를 지운다.

15 12
2 3 4 5 6 7 8 9 10 11 12 13 14 15
2 4 6 8 9 10 12 14 3 5 15 6 7 

'''
import sys, math
input = sys.stdin.readline

n, k = map(int, input().split())

def get_prime(num) :
    if num != 0 :
        cnt = 0
        for i in range(2, int(math.sqrt(num)) + 1) :
            if num % i == 0 :
                cnt += 1 
                break
        
        if cnt == 0 : 
            return True
        else :
            return False

arr = [0, 0]
for i in range(2, n + 1) :
    arr.append(i)

# print(arr)
cnt = 0
answer = ""
for i in arr :
    if get_prime(i) :
        
        for j in range(0, len(arr), i) :
            if arr[j] != 0 :
                cnt += 1 
                if cnt == k :
                    # answer = arr.index(arr[j])
                    answer = arr[j]
                    break
                arr[j] = 0 
    
    if answer != "" :
        break
                
        # print(cnt)
        # print(arr)
print(answer)


# print(arr)


