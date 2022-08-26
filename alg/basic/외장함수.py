import glob
print(glob.glob("*.py")) #확장자가 py인 모든 파일

os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) #현재 디렉토리

folder = "sample_dir"

if os.path.exists(floder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir())

time = 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

timedelta : 둘 날짜 사이의 간격
today = datetime.date.today() #오늘 날짜 저장
td = datetime.timedelta(days=100) #100일 저장
print("우리가 만난 100일은", today +td)