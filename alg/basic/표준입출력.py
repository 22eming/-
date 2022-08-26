print("Python", "Java") #한칸 띄어쓰기
print("Python", "Java", sep="") #붙여쓰기
print("Python", "Java", sep=",", end="?") #end = 문장의 끝부분을 ?로 변경

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject,score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") #왼쪽 정렬, 오른쪽 정렬

#은행 대기순번표
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) #없는 번호는 0으로 채움

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")