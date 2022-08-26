url = "http://google.com"
password = url.replace("http://", "")
password = password[:password.index(".")]
password = password[:3] + str(len(password)) + str(password.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다." .format(url, password))