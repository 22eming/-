from math import log2


def check(num2bin, parent):
    mid = len(num2bin) // 2
    if len(num2bin) == 0:
        return True
    else:
        sub_root = num2bin[mid] == "1"

    if sub_root and not parent:
        return False
    else:
        return check(num2bin[:mid], sub_root) and check(num2bin[mid + 1 :], sub_root)


def pre(num):
    if num == 1:
        return 1

    num2bin = bin(num)[2:]
    digit = 2 ** (int(log2(len(num2bin))) + 1) - 1
    num2bin = "0" * (digit - len(num2bin)) + num2bin
    if num2bin[len(num2bin) // 2] == "1" and check(num2bin, True):
        return 1
    else:
        return 0


def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(pre(number))

    return answer