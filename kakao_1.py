def solution(arr):
    answer = True
    reArr = arr.reverse()
    inArr = []

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    for num in arr:
        if num > len(arr):
            answer = False
            break

        if arr.count(num) > 1:
            answer = False
            break

        if num in inArr:
            answer = False
            break

        else:
            inArr.append(num)

    return answer


assert solution([4, 1, 3, 2]) == True
assert solution([4, 1, 3]) == False

# TESTCASE 통과
# 효율성 테스트 비통과