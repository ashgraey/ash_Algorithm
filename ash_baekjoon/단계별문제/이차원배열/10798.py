'''
세로읽기//

입력//
ABCDE
abcde
01234
FGHIJ
fghij

출력//
Aa0FfBb1GgCc2HhDd3IiEe4Jj
'''
import sys
input = sys.stdin.readline

# words = []
# for _ in range(5) :
#     word = list(input())
#     words.append(word)

# words = [
#     "ABCDE",
#     "abcde",
#     "01234",
#     "FGHIJ",
#     "fghij"
# ]

words = [
    "AABCDD",
    "afzz",
    "09121",
    "a8EWg6",
    "P5h3kx"
]
# 길이값 맥스

# print(words[0][0])
answer = ""
for i in range(len(words)) :
    for j in range(len(words[i])) :
        # print(words[j][i], end = "")
        answer += words[j][i]

print(answer)

