'''
문제 일곱난쟁이//
'''
import sys
input = sys.stdin.readline

arr = []
for _ in range(9) : 
    arr.append(int(input()))
# print(arr)

val = sum(arr) - 100

size = len(arr)
for i in range(size) :
    for j in range(size) :
        if i != j :
            if arr[i] + arr[j] == val :
                idx1 = i
                idx2 = j
                break

del(arr[idx1])
del(arr[idx2])
arr.sort()
for i in arr :
    print(i)  

