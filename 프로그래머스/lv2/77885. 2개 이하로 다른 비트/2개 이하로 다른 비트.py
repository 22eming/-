def solution(numbers):
    answer = []
    for number in numbers:
        number = bin(number)
        if "0" not in number[2:]:
            answer.append( int("0b10" + number[3:], 2) )
        elif(number[-1] == "0"):
            answer.append( int(number[:-1] + "1", 2) )
        else:
            i = number.rindex("0")
            answer.append( int(number[:i] + "10" + number[i+2:] ,2) )
    return answer