'''
집합//
'''

import sys
input = sys.stdin.readline

n = int(input())

s = set()
# print(s)
for _ in range(n) :
    user = input().strip()
    user = user.split(" ")
    # user[1] = int(user[1])


    if user[0] == "add" :
        if int(user[1]) not in s :
            s.add(int(user[1]))
        else :
            continue
    
    elif user[0] == "remove" :
        if int(user[1]) in s :
            s.remove(int(user[1]))
        else :
            continue
    
    elif user[0] == "check" :
        if int(user[1]) in s :
            print(1)
        else :
            print(0)
        
    elif user[0] == "toggle" :
        if int(user[1]) not in s :
            s.add(int(user[1]))
        else :
            s.remove(int(user[1]))
    
    elif user[0] == "all" :
        s = {*range(1, 21)}

    elif user[0] == "empty" :
        s = set()

    # print(s)

# user = input().strip()
# user = user.split(" ")
# print(user)