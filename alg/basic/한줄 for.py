#출석 번호가 1 2 3 4 , 앞에 100을 붙이기로 함
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor","I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor","I am groot"]
students = [i.upper() for i in students]
print(students)