'''
문제 123 더하기//

'''
import sys
input =  sys.stdin.readline

n = int(input())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
# print(dp)

for i in range(4, 11) :
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

idx = []
for i in range(n) :
    idx.append(int(input()))

for i in idx :
    print(dp[i])
