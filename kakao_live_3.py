def solution(food_times, k):
    now_idx = 0
    max_idx = len(food_times)
    answer = 0

    for i in range(k):
        if food_times[now_idx] == 0:
            while food_times[now_idx] == 0:
                now_idx += 1

        food_times[now_idx] -= 1
        now_idx +=1

        if now_idx == max_idx:
            now_idx = 0

    answer = now_idx + 1
    return answer

assert solution([3,1,2], 5) == 1