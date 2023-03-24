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
# import sys
# input = sys.stdin.readline

words = []
for _ in range(5) :
    word = input()
    words.append(word)

# words = [
#     "ABCDE",
#     "abcde",
#     "01234",
#     "FGHIJ",
#     "fghij"
# ]

# words = [
#     "AABCDD",
#     "afzz",
#     "09121",
#     "a8EWg6",
#     "P5h3kx"
# ]
# 길이값 맥스
max = 0 
for i in words : 
    if max < len(i) :
        max = len(i)

# print(max)
wordList = []
for word in words :
    if len(word) < max :
        size = max - len(word)
        # print(size)
        for j in range(size) :
            word += "*"
            # print(word)
        wordList.append(word)
    elif len(word) >= max :
        wordList.append(word)
# print(wordList)

answer = ""
for i in range(len(wordList[0])) :
    for j in range(len(wordList)) :
        if wordList[j][i] != "*" :
            answer += wordList[j][i]

print(answer)



# print(words[0][0])
# answer = ""
# for i in range(len(words)) :
#     for j in range(len(words[i])) :
#         # print(words[j][i], end = "")
#         answer += words[j][i]

# print(answer)

