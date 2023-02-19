def convert_time(time):
    """_summary_
    Args:
        time (str): "HH:MM"형식의 시간 입력

    Returns:
        int: 분 형식
    """
    h, m = map(int, time.split(":"))
    return h*60 + m

def solution(book_time):
    answer = 0
    book_time = sorted([list(map(convert_time, times)) for times in book_time])
    end_times = []
    for time in book_time:
        start, end = time
        for idx, end_time in enumerate(end_times):
            if start >= end_time+10:
                del end_times[idx]
                break
        else:
            answer += 1
        end_times.append(end)
    return answer