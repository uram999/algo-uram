def solution(N, stages):
    stage_info = []
    answer = []
    #
    for i in range(N):
        if i not in stage_info:
            stage_info.append({"floor": i+1, "dodal": 0, "stay": 0, "fail_rate": 0})

    for per in stages:
        for i in range(N):
            if i > per-1:
                break
            elif i == per-1:
                stage_info[i]["dodal"] += 1
                stage_info[i]["stay"] += 1
            else:
                stage_info[i]["dodal"] += 1

            stage_info[i]["fail_rate"] = stage_info[i]["stay"]/stage_info[i]["dodal"]

    for data in sorted(stage_info, key=lambda x: x["fail_rate"], reverse=True):
        answer.append(data["floor"])

    return answer


assert solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3,4,2,1,5]