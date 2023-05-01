'''
문제 수들의 합//

알고리즘//
수학
그리디

키워드//

'''

n = int(input())

sum = 0
cnt = 0 
for i in range(1, n + 1) :
    sum += i 
    cnt += 1 

    if sum > n : 
        cnt -= 1 
        break

print(cnt)