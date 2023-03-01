def solution(food):
    answer = ''
    for idx, i in enumerate(food):
        if not idx: continue
        answer += f"{idx}"*(i//2)
    return f"{answer}0{answer[::-1]}"