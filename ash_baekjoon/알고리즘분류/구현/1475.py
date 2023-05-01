'''
문제 방번호//

알고리즘//
구현

키워드//
잘못된 방향으로 생각했다.
중복이 되면 set를 하나 더 사용해하는게 키워드, 6과 9만 예외처리해주면 쉬운 문제 

예외처리// 6이나 9는 두번 사용이 가능하니 서로 크기를 비교해서 작은쪽 인덱스에 += 1을 해준다. 

나머지는 값에 맞는 인덱스에 += 1씩 해준다. 
결과적으로 배열에서 max값이 최종 사용한 set의 수가 된다.
오히려 구현이 더 어려운듯  
'''
import sys
input = sys.stdin.readline

n = input().rstrip()
nums = [0] * 10 

for i in n :
    i = int(i)

    if i == 6 or i == 9 :
        if nums[6] <= nums[9] :
            nums[6] += 1 
        else :
            nums[9] += 1
    
    else :
        nums[i] += 1 

print(max(nums))
