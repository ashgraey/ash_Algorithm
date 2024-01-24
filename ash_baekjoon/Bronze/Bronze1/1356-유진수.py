#1236

N = int(input())

# slicing
N = str(N)
# N_fir = N[:1]

ck = False
if len(N) > 1 :
    for i in range(len(N)) :
        N_fir = N[:i + 1]
        fir_tot = 1
        for j in N_fir : 
            fir_tot *= int(j)
        
        # print("1 : ", fir_tot)

        N_sec = N[i + 1:]
        # print(N_sec)
        # break
        sec_tot = 1
        for j in N_sec : 
            sec_tot *= int(j)
        # print("2 : ", sec_tot)

        if fir_tot == sec_tot :
            ck = True
            break

if ck :
    print("YES")
else :
    print("NO")