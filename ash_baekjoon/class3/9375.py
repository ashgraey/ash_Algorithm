'''
문제 패션왕 신혜빈//
'''
import sys

input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    case = int(input())

    wear_dict = {}
    for i in range(case) :
        wear = input().strip()
        wear = wear.split(" ")
        wear_dict[wear[1]] = wear[0]

print(wear_dict)