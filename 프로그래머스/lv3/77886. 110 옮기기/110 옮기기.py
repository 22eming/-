def solution(s):
    def f(x):
        left, I, IIO = '', 0, 0
        for i in x:
            if i == '1':
                I += 1
            elif I > 1:
                I -= 2
                IIO += 1
            else:
                left += '10' if I > 0 else '0'
                I = 0
        return left + '110' * IIO + '1' * I

    return [f(x) for x in s]