"""
bookRent 는 책 대여횟수이다. 책은 총 5권이다.
5권부터 1권씩 줄여가면서 책권수보다 배열전체를 검사해서 대여회수가 크거나 같으면 카운트를 한다.
그카운트가 책권수 이상이면 책권수를 출력후 종료.

    [얘시1] 3, 0 , 6 , 1 ,5 이면 
        5이상인수는 (6,5) 두개이다 , 
        4이상인수는 (6,5) 두개이다,
        3이상인수는 (6,5,3) 세개이고 , 책권수와 카운트가 일치하므로 책3권에서 종료.

    [예시2] 10000, 9999, 9998 , 9997 , 4

        5이상인수는 (1000,9999,9998,9997) 4개이다,
        4이상인수는 (1000,9999,9998,9997,4) 5개이다. 책 4권에서 종료.

    [예시3] 0, 1, 2, 3, 4

        5이상인수는 0
        4이상인수는 1
        3이상인수는 2
        2이상인수는 3 책2에서 종료 
"""

def solution(rent):
    size = len(rent)
    # print(size)
    for _ in range(len(rent)) :
        cnt = 0 
        for j in rent :
            # print(j)
            if j >= size :
                cnt += 1 
        # print(cnt)
        if cnt >= size :
            break
        else :
            size -= 1

    return size

    

bookRent =  [3, 0, 6, 1, 5]
# bookRent = [10000, 9999, 9998, 9997, 4]
bookRent = [0, 1, 2, 3, 4]
result = solution(bookRent)
print(result)








