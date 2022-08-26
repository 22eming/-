try:
    print("나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫번재 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2} ".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)



#에러 발생

try:
    print("한 자리 숫자 나누기 계산기")
    num1 = (int(input("첫번재 숫자를 입력하세요 : ")))
    num2 = (int(input("두번재 숫자를 입력하세요 : ")))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2} ".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력")


# 사용자 정의 에러

class BignumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg


try:
    print("한 자리 숫자 나누기 계산기")
    num1 = (int(input("첫번재 숫자를 입력하세요 : ")))
    num2 = (int(input("두번재 숫자를 입력하세요 : ")))
    if num1 >= 10 or num2 >= 10:
        raise BignumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2} ".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력")
except BignumberError as err:
    print("에러발생: 한자리 숫자만 입력")
    print(err)
finally:
    print("계산기를 이용해주셔서 감사합니다.")

#finally