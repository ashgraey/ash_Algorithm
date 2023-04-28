'''
문제 3의 배수//
'''
import sys
input = sys.stdin.readline
n = input().rstrip()

cnt = 0
while True :

    if len(n) == 1 :
        break

    temp = 0     
    for i in n : 
        temp += int(i)
    

    n = str(temp)
    cnt += 1 
    # print(n)
print(cnt)
if int(n) % 3 == 0 :
    print("YES")
else :
    print("NO")