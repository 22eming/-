def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = int(input("키를 입력해주세요. "))
gender = str(input("성별을 입력해주세요. "))
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}입니다. ".format(height, gender, weight))