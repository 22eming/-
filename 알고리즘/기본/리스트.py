subway = [10, 20, 30]

subway = ["조세호", "유재석", "이광수"]

print(subway.index("조세호"))

subway.append("하하")

subway.insert(1,"정형돈")

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄

print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬

num_list = [1,5,6,7,8]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#지우기
num_list.clear()
print(num_list)

다양한 자료와 함께

num_list = [4,1,2,8,9]
mix_list = ["조세호", 20, True]

num_list.extend(mix_list)
print(num_list)