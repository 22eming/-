from collections import defaultdict

cus, line_n = map(int, input().split())
m = defaultdict(dict)
for i in range(line_n):
	s, e, v = map(int, input().split())
	m[s][e] = v

stack = list(m.keys())

while stack != []:
	s = stack.pop()
	print(m[s])