'''
문제 절대값 힙//
'''
def LCS_length(s1, s2):
    m = len(s1)
    n = len(s2)
    # LCS를 저장할 테이블 생성
    L = [[0] * (n+1) for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
        for k in L :
            print(k)
        print()

    return L[m][n]

s1 = input()
s2 = input()
print(LCS_length(s1, s2))