def solution(record):
    user_data = {}
    log = []
    int2str = {1:"님이 들어왔습니다.", 0:'님이 나갔습니다.'}
    for rec in record:
        in_out, uid, *name = rec.split()
        if in_out != "Leave":
            user_data[uid] = name[0]
        if in_out == "Enter":
            log.append([uid, 1])
        elif in_out == "Leave":
            log.append([uid, 0])

    for i in range(len(log)):
        log[i] = user_data[log[i][0]] + int2str[log[i][1]]
    return log