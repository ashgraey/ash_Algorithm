# https://school.programmers.co.kr/learn/courses/30/lessons/12915
'''
문제 설명
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 
각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

제한 조건
strings는 길이 1 이상, 50이하인 배열입니다.
strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
모든 strings의 원소의 길이는 n보다 큽니다.
인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.

입출력 예
strings	                n	return
["sun", "bed", "car"]	1	["car", "bed", "sun"]
["abce", "abcd", "cdx"]	2	["abcd", "abce", "cdx"]
'''
# n이 기준이 되는 index
# n 기준으로 정렬
def solution(strings, n):
    new = []
    for i in strings :
        new.append(i[n] + i) # *요구하는 인덱스의 값을 맨앞으로 보내기(정렬을 용이하게 하기 위함)*
    new.sort()
    # print(new)

    answer = []
    for i in new :
        answer.append(i[1:]) # 슬라이싱 [1:] 시작인덱스부터 모든 값을 추출한다. 결과적으로 0인덱스 삭제
    # print(answer)

    
    return answer


strings =["abce", "abcd", "cdx"]
n = 2
a = solution(strings , n)
print(a)