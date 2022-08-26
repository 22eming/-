absent = [2, 5] #결석
no_book = [7] # 책을 안 가져옴
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 와".format(student))
        break
    print("{0}, 책을 읽어봐.".format(student))
