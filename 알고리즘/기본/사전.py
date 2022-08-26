cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet[5]) #없는값은 오류
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet) #키 in 변수
print(5 in cabinet)

#사전 추가
cabinet = {"A-30":"유재석", "B-100":"김태호"}
cabinet["A-30"] = "김종국"
cabinet["C-20"] = "조세호"

#사전 제거
del cabinet["A-30"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

cabinet.clear()
print(cabinet)