'''
문제 피보나치수5//

알고리즘//
수학 
구현

키워드//
피보나치수 구현문제 
별다르게 다를건 없다.
'''
def fibonachi(n) :
    if n == 0 or n == 1 :
        return n
    else : 
        a = 0
        b = 1 
        c = a + b
        for i in range(2, n) :
            a = b
            b = c 
            c = a + b
        return c

n = int(input())
print(fibonachi(n))