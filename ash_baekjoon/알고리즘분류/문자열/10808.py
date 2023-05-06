'''
문제 알파벳 개수//

알고리즘//
문자열
구현

키포인트//
1. 알파벳 sample을 만든다. 
2. word를 기준으로 반복문을 돌리고 요소가 sample안에 있는지 검사한다. 
3. sampe안에 있으면 sample에서 요소의 인덱스를 추출한다. 
4. cnt[idx]에 1씩 더한다.
'''

import sys
input = sys.stdin.readline

word = input().rstrip()
sample = "abcdefghijklmnopqrstuvwxyz"

cnt = [0 for _ in range(len(sample))]
# cnt2 = [0] * len(sample) 위의 식과 결과값은 동일하게 나온다.
# print(cnt)

for i in range(len(word)) :
    if word[i] in sample :
        idx = sample.index(word[i])
        # print(idx)
        cnt[idx] += 1

# print(cnt)
for i in cnt :
    print(i, end = " ")

# print(cnt2)