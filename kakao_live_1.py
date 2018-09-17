
def solution(record):
    record.reverse()
    id_log = dict()
    answer = []

    for log in record:
        content = log.split(' ')

        if len(content) > 2:
            if content[1] not in id_log:
                id_log[content[1]] = content[2]

            if content[0] =="Change":
                id_log[content[1]] = content[2]

        if content[0] != "Change":
            name = id_log[content[1]]
            if content[0] == "Enter":
                logstr = name+"님이 들어왔습니다."
            if content[0] == "Leave":
                logstr = name+"님이 나갔습니다."

            answer.append(logstr)

    answer.reverse()
    return answer


assert solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]) == ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]