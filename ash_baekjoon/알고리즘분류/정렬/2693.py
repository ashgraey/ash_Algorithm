'''
문제 N번째 큰 수//

알고리즘//
정렬

키포인트// 
reverse정렬 시켜서 2번 인덱스의 값만 찾아오면 될듯
'''
import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    arr = list(map(int, input().split()))

    arr_sorted = sorted(arr, reverse = True)
    
    print(arr_sorted[2])