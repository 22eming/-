import pickle

for n in range(1, 3):
    with open(str(n)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0}주차 주간보고 - ".format(n))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")
    report_file.close()
