
T = int(input())

for _ in range(T) :
    N = int(input())
    sList = []
    lList = []
    for _ in range(N) :
        S, L = input().split()
        sList.append(S)
        lList.append(int(L))
    
    # print(lList)
    maxL = max(lList)
    # print(max)
    idx = lList.index(maxL)
    # print(idx)
    print(sList[idx])

