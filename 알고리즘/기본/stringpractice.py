python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper()) #대문자냐?
print(len(python)) #길이
print(python.replace("Python", "Java")) #파이선을 자바로 교체

Index = python.index("n") #몇번째
print(Index) 
Index = python.index("n", Index + 1)
print(Index)

print(python.find("Python")) #값 없을시 -1 있을시 0
#index 에서는 오류
print(python.count("n")) #n이 몇번
