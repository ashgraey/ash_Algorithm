import sys

A, B = sys.stdin.readline().split()

# print(A, B)
# total = 0
# for i in A :
#     temp = 0
#     for j in B :
#         temp += int(i) * int(j)
#     total += temp

# print(total)
# A_tot = 0
# for i in A :
#     A_tot += int(i)

# total = 0 
# for i in B :
#     total += A_tot * int(i)
# print(type(total))

A_tot = 0
for i in A :
    A_tot += int(i)

B_tot = 0
for i in B :
    B_tot += int(i)

print(A_tot * B_tot)