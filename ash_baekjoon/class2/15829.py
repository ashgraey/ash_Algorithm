'''

'''

import sys
input = sys.stdin.readline

abc = "abcdefghijklmnopqrstuvwxyz"
mod = 1234567891

l = int(input())
words = input().strip()

# wordsList = []
# for i in words :
#     wordsList.append(i)
idxList = []
for i in words :

    for j in abc :
        if i == j :
            jIdx = abc.index(j) + 1
            break
    
    idxList.append(jIdx)

# print(idxList)

total = 0
for i in range(len(idxList)) :
    total += idxList[i] * pow(31, i)

print(total % mod)




