'''
문제 단어 뒤집기//

알고리즘//
구현, 문자열

키포인트//
<문자열을 뒤집는 방법>
s = "Hello World"
1.슬라이싱을 사용
reversed_s = s[::-1]
역순을로 잘라내는 슬라이싱

2. reversed()와 join()을 사용
reversed_s = ''.join(reversed(s))
'''
import sys
input = sys.stdin.readline

tc = int(input())

answer = []
for _ in range(tc) : 
    word = input().rstrip()
    wordList = word.split(" ")
    for i, v in enumerate(wordList) :
        reverse_v = v[::-1]
        wordList[i] = reverse_v
    # answer.append(' '.join(wordList))
    # answer.append(wordList)
    print(' '.join(wordList)) # 어레이를 문자열로 출력
# # print(answer) 
# for v in answer :
#     print(v)