'''
문제 포켓몬 마스터 이다솜//
230413
당했다...
처음부터 키를 두개로 딕셔너리에 저장해서 
그냥 출력하면 해결되는거였음

하나의 키로만 저장해서 검색을 통해 출력을 하려고 하니
계속해서 시간초과남..
쉽지않네..

내장함수//
isdigit() : 문자열 구성이 숫자면 True, 아니면 False를 반환
문자열이 숫자인지 확인하고 싶을 때 사용하면 좋다
주의할점은 오로지 숫자로만 구성되어 있어야한다. 기호나 문자가 포함되어있으면 False를 반환
'''
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# pokemon_dict = {}
# for i in range(1, n + 1) :
#     pokemon_dict[str(i)] = input().strip()

# # print(pokemon_dict)

# # number = "0123456789"
# for _ in range(m) :
#     find = input().strip()

#     # if find[0] in number :
#     #     # key = pokemon_dict.get(find)
#     #     # print(key)
#     #     print(pokemon_dict[find])
    
#     # else : 
#     #     print(' '.join([k for k, v in pokemon_dict.items() if v == find]))

#     for k, v in pokemon_dict.items() :
#         if k == find :
#             print(pokemon_dict[k])
#             break
        
#         elif v == find :
#             print(k)
#             break


# 인터넷 정답
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

poke_dict = {}
for i in range(1, n + 1) :
    a = input().rstrip()
    poke_dict[str(i)] = a
    poke_dict[a] = str(i)

# print(poke_dict)
# number = "0123456789"
for _ in range(m) : 
    find = input().rstrip()
    print(poke_dict[find])
    # if find[0] in number :
    #     print(poke_dict[find])
    # else : 
    #     print(poke_dict[find])
