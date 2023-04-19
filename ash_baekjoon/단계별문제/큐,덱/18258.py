'''
문제 큐2//
'''
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

que = deque()
for _ in range(n) :
    user = input().rstrip()
    # user = user.split(" ")

    if "push" in user :
        user = user.split(" ")
        que.append(int(user[1]))
    
    elif user == "pop" :
        if len(que) == 0 :
            print(-1)
        else :
            print(que.popleft())
        
    elif user == "size" :
        print(len(que))

    elif user == "empty" :
        if len(que) == 0 : 
            print(1)
        else :
            print(0)
    
    elif user == "front" :
        if len(que) == 0 :
            print(-1)
        else :
            print(que[0])

    elif user == "back" :
        if len(que) == 0 :
            print(-1)
        else :
            print(que[-1]) 