'''
가로수 문제//
'''
import sys
def gcd_func(a, b) :
    if a < b :
        a, b = b, a
    
    while b > 0 :

        a %= b
        a, b = b, a
    
    return a

input = sys.stdin.readline

tc = int(input())

trees = [int(input()) for _ in range(tc)]
# print(trees)

gaps = []
for i in range(tc - 1) :
    gab = trees[i] - trees[i + 1]
    gaps.append(-gab)

gaps = list(set(gaps))
# print(gaps)

# print(gaps)
# 간격 하나마다 최대공약수 구하기
fir_tree = gaps[0]
for i in range(1, len(gaps)) :
    tree_gcd = gcd_func(fir_tree, gaps[i])
    # print(tree_gcd) 
# print(tree_gcd)

cnt = 0 
for gap in gaps :
    cnt += (gap // tree_gcd) - 1 # 간격을 최대공약수로 나누고 1을 빼주면 심을 나무의 숫자

print(cnt)