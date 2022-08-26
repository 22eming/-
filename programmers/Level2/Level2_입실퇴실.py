def solution(enter, leave):
    answer = [0 for _ in range(len(enter))]
    room = []
    for i in enter:
        if len(room) >= 1:
            for ii in room:
                answer[ii-1] += 1
                answer[i-1] += 1

        room.append(i)

        leave_1 = []
        for j in leave:
            if j in room:
                room.remove(j)
                leave_1.append(j)
            else:
                for k in leave_1:
                    leave.remove(k)
                break

    return answer

print(solution([1, 4, 2, 3], [4, 1, 2, 3]))

# 1. 입실먼저 퇴실 나중 12 21
# 2. 2명 보다 나중에 입실한 사람이 나중에 입실한 사람보다 빨리 퇴실 123 132
# 3. 2명 보다 나중에 입실한 사람이 둘보다 빨리 퇴실 123 213 
